#!/usr/bin/env python3
"""Trial-only isolated recreation; no registry push or production connection."""

import datetime
import json
from pathlib import Path
import subprocess
import sys
import time
import urllib.error
import urllib.request
import uuid

COMMIT = "4600202bad42da0c5ffb11d83ce8364671293d3d"
BASE_URL = "http://127.0.0.1:18090"


def run(*args, **kwargs):
    return subprocess.run(args, check=True, text=True, **kwargs)


def request(path, payload=None):
    data = None if payload is None else json.dumps(payload).encode()
    req = urllib.request.Request(BASE_URL + path, data=data,
                                 headers={"Content-Type": "application/json"})
    try:
        response = urllib.request.urlopen(req, timeout=2)
    except urllib.error.HTTPError as error:
        response = error
    with response:
        return response.status, json.load(response)


def main():
    source = Path(sys.argv[1]).resolve()
    actual = run("git", "-C", str(source), "rev-parse", "HEAD",
                 capture_output=True).stdout.strip()
    if actual != COMMIT:
        raise RuntimeError("Expected the reviewed, pinned application commit")
    suffix = uuid.uuid4().hex[:10]
    image = "is373-recreation:" + suffix
    name = "is373-recreation-" + suffix
    try:
        run("docker", "build", "--build-arg", "COMMIT_SHA=" + COMMIT,
            "--build-arg", "BUILT_AT=" + datetime.datetime.now(
                datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "--tag", image, str(source))
        run("docker", "run", "--detach", "--name", name,
            "--user", "10001:10001", "--read-only", "--cap-drop=ALL",
            "--security-opt=no-new-privileges:true", "--pids-limit=128",
            "--tmpfs=/tmp:rw,noexec,nosuid,nodev,size=64m,mode=1777",
            "--publish", "127.0.0.1:18090:8000", "--env", "APP_ENV=production", image)
        deadline = time.monotonic() + 45
        while True:
            try:
                status, health = request("/health")
                if status == 200 and health.get("status") == "ok":
                    break
            except (OSError, ValueError):
                pass
            if time.monotonic() >= deadline:
                raise RuntimeError("The isolated container did not become ready in 45 seconds")
            time.sleep(0.5)
        if health.get("commit") != COMMIT or health.get("environment") != "production":
            raise RuntimeError("Health does not identify the expected production-mode commit")
        positive = request("/api/calculate", {"a": 6, "b": 7, "operation": "multiply"})
        negative = request("/api/calculate", {"a": 6, "b": 0, "operation": "divide"})
        if positive != (200, {"result": 42.0}):
            raise RuntimeError("Six times seven did not return 42")
        if negative[0] != 400 or negative[1].get("detail", {}).get("code") != "division_by_zero":
            raise RuntimeError("Zero divisor did not return the documented HTTP 400 error")
        image_id = run("docker", "image", "inspect", image, "--format", "{{.Id}}",
                       capture_output=True).stdout.strip()
        print(json.dumps({"source_commit": actual, "image_id": image_id,
                          "target": BASE_URL, "health": health,
                          "positive": positive, "negative": negative}, indent=2))
        print("PASS: isolated app source rebuild, release identity, positive and negative API cases")
    finally:
        subprocess.run(["docker", "rm", "--force", name], stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=False)
        subprocess.run(["docker", "image", "rm", image], stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=False)


if __name__ == "__main__":
    main()
