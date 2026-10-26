"""Behavior checks in disposable repositories; no server access or network."""

import importlib.util
import os
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

MODULE = Path(__file__).resolve().parents[1] / "scripts" / "check_docs.py"
SPEC = importlib.util.spec_from_file_location("check_docs", MODULE)
CHECKER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECKER)


class PublicationChecks(unittest.TestCase):
    def setUp(self):
        environment = patch.dict(os.environ, {"GIT_CONFIG_NOSYSTEM": "1", "GIT_CONFIG_GLOBAL": os.devnull})
        environment.start()
        self.addCleanup(environment.stop)
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "clone"
        self.root.mkdir()
        self.git("init", "--quiet")
        self.git("config", "core.excludesFile", os.devnull)

    def git(self, *args):
        return subprocess.run(
            ["git", *args], cwd=self.root, check=True, capture_output=True,
            env={**os.environ, "GIT_CONFIG_NOSYSTEM": "1", "GIT_CONFIG_GLOBAL": os.devnull},
        )

    def write(self, name, contents):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(contents, encoding="utf-8")

    def messages(self):
        return [message for _, _, message in CHECKER.check(self.root)]

    def test_real_links_images_encoded_spaces_and_fenced_examples(self):
        self.write("docs/my diagram.svg", "<svg/>")
        self.write("docs/guide.md", "# Setup\n")
        self.write("README.md", """[Guide](docs/guide.md#setup)
![Diagram](docs/my%20diagram.svg)
[Guide again][guide]
[guide]: <docs/guide.md>
[Internet](https://example.test/missing) [Anchor](#start)
```sh
[Example](missing-example.md)
```
`[Inline example](missing-inline.md)`
""")
        self.assertEqual([], self.messages())
        self.write("README.md", "[Broken](docs/missing.md)\n")
        self.assertEqual(["local link target does not exist"], self.messages())

    def test_lexical_and_symlink_escape_are_rejected_before_reading(self):
        outside = self.root.parent / "outside.md"
        outside.write_text("Outside document", encoding="utf-8")
        self.write("README.md", "[Outside](../outside.md)\n[Encoded](%2e%2e/outside.md)\n")
        self.assertEqual(2, len(self.messages()))
        (self.root / "borrowed.md").symlink_to(outside)
        self.assertIn("file or symlink points outside this clone", self.messages())
        self.write("README.md", "[Absolute](/etc/passwd)\n[File](file:///etc/passwd)\n[Windows](C:/Users/private.md)\n")
        self.assertEqual(4, len(self.messages()))

    def test_secret_guard_does_not_echo_values_and_allows_placeholders(self):
        secret = "sensitive" + "-example"
        self.write("README.md", "https://student:" + secret + "@example.test\n"
                   + "-----BEGIN " + "OPENSSH PRIVATE KEY-----\n")
        findings = CHECKER.check(self.root)
        self.assertEqual(2, len(findings))
        self.assertNotIn(secret, repr(findings))
        self.write("README.md", "https://USERNAME:" + "${PASSWORD}@example.test\n"
                   + "OPENAI_API_KEY=YOUR_KEY\n")
        self.write(".env.example", "PASSWORD=REPLACE_ME\n")
        self.assertEqual([], self.messages())

    def test_ignored_private_capture_stays_private_but_tracked_env_fails(self):
        self.write(".gitignore", ".private/\n.env\n")
        self.write(".private/server.txt", "-----BEGIN " + "RSA PRIVATE KEY-----\n")
        self.write(".env", "PASSWORD=not-a-real-secret\n")
        self.assertEqual([], self.messages())
        self.git("add", "--force", ".env")
        self.assertEqual(["credential filename must not be published"], self.messages())


if __name__ == "__main__":
    unittest.main()
