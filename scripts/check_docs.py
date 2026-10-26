#!/usr/bin/env python3
"""Small, offline publication checks; not a server or documentation grader."""

import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


LINK = re.compile(r'!?\[[^\]\n]*\]\(\s*(<[^>\n]*>|[^\s)\n]+)(?:\s+["\'][^\n]*?["\'])?\s*\)')
REFERENCE = re.compile(r'^\s{0,3}\[[^\]\n]+\]:\s*(<[^>\n]*>|\S+)')
FENCE = re.compile(r'^\s{0,3}(`{3,}|~{3,})')
PRIVATE_KEY = re.compile(r'-----BEGIN (?:[A-Z0-9]+ )*PRIVATE KEY-----')
CREDENTIAL_URL = re.compile(r'\b[a-z][a-z0-9+.-]*://([^\s<>/"\']+):([^\s<>/@"\']+)@', re.I)
LIMIT = "Checks cover local document links and selected secret patterns only; not factual, server, or recreation proof."


def published_files(root):
    """Use Git's ignore rules; tracked files remain checked even if ignored now."""
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=root, check=True, capture_output=True,
    )
    return sorted(set(result.stdout.decode("utf-8").split("\0")) - {""})


def contained(path, root):
    """Check both normalized lexical paths and symlink targets before opening."""
    try:
        path.absolute().relative_to(root)
        path.resolve().relative_to(root)
        return True
    except (ValueError, OSError, RuntimeError):
        return False


def credential_filename(path):
    name = path.name.lower()
    dotenv = (name == ".env" or name.startswith(".env.")) and not name.endswith(".example")
    ssh_key = name in {"id_rsa", "id_dsa", "id_ecdsa", "id_ed25519"}
    return dotenv or ssh_key or name in {"privkey.pem", "private.pem"} or name.endswith((".key", ".p12", ".pfx")) or bool(
        re.fullmatch(r"(?:private[-_]?key|.+[-_]private[-_]?key)\.(?:pem|key)", name)
    )


def placeholder(value):
    return value in {"PASSWORD", "YOUR_PASSWORD", "REDACTED"} or bool(
        re.fullmatch(r"\$\{[A-Z_][A-Z0-9_]*\}", value)
    )


def local_targets(lines):
    """Inline links/images and reference definitions; examples in fences are inert."""
    fence = None
    for number, line in enumerate(lines, 1):
        marker = FENCE.match(line)
        if marker:
            token = marker.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence:
            continue
        line = re.sub(r"(`+).*?\1", "", line)
        for match in LINK.finditer(line):
            yield number, match.group(1).strip("<>")
        definition = REFERENCE.match(line)
        if definition:
            yield number, definition.group(1).strip("<>")


def check(root):
    root = Path(root).resolve()
    errors = []
    for relative in published_files(root):
        path = root / relative
        if not contained(path, root):
            errors.append((relative, 1, "file or symlink points outside this clone"))
            continue
        if credential_filename(path):
            errors.append((relative, 1, "credential filename must not be published"))
            continue
        if not path.is_file():
            continue  # Staged deletions and submodules are not document contents.
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            continue
        except OSError:
            errors.append((relative, 1, "file could not be read"))
            continue
        for number, line in enumerate(lines, 1):
            if PRIVATE_KEY.search(line):
                errors.append((relative, number, "private-key block must not be published"))
            if any(not placeholder(match.group(2)) for match in CREDENTIAL_URL.finditer(line)):
                errors.append((relative, number, "URL contains credentials; use placeholders"))
        if path.suffix.lower() != ".md":
            continue
        for number, target in local_targets(lines):
            try:
                parsed = urlsplit(target)
                if parsed.scheme == "file" or re.match(r"^[A-Za-z]:[\\/]", target):
                    raise ValueError("machine-specific path")
                if parsed.scheme or parsed.netloc:
                    continue  # No network requests, external URL or anchor validation.
                decoded = unquote(parsed.path)
                if not decoded:
                    continue
                if Path(decoded).is_absolute():
                    raise ValueError("absolute path")
                destination = path.parent / decoded
                if not contained(destination, root):
                    errors.append((relative, number, "local link leaves this clone"))
                elif not destination.exists():
                    errors.append((relative, number, "local link target does not exist"))
            except (ValueError, OSError, RuntimeError):
                errors.append((relative, number, "local link has an unsafe or invalid path"))
    return errors


def main():
    root = Path(__file__).resolve().parents[1]
    try:
        errors = check(root)
    except (subprocess.CalledProcessError, UnicodeError):
        print("Run this check inside the Git clone.", file=sys.stderr)
        return 2
    for path, line, message in errors:
        print(f"{path}:{line}: {message}")
    print(f"{len(errors)} publication problem(s). {LIMIT}")
    return bool(errors)


if __name__ == "__main__":
    sys.exit(main())
