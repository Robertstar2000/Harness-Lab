"""Check that committed HTML is verified locally and a stale copy fails clearly."""
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "sync-publication.py"
ORIGIN = "https://mars-harness-lab-v5.tallman-equi-9130.chatgpt.site"


class PublicationSyncTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "scripts").mkdir()
        (self.root / "dist").mkdir()
        (self.root / "scripts" / "sync-publication.py").write_bytes(SCRIPT.read_bytes())
        self.html = b"<!doctype html><title>Canonical source</title>\n"
        (self.root / "publication-manifest.json").write_text(json.dumps({
            "origin": ORIGIN,
            "site_version": 22,
            "site_source_commit": "test",
            "files": [{
                "path": "dist/index.html",
                "bytes": len(self.html),
                "sha256": hashlib.sha256(self.html).hexdigest(),
            }],
        }))

    def run_sync(self):
        return subprocess.run(
            [sys.executable, str(self.root / "scripts" / "sync-publication.py")],
            capture_output=True, text=True, timeout=10,
        )

    def test_matching_canonical_html_needs_no_network(self):
        (self.root / "dist" / "index.html").write_bytes(self.html)
        result = self.run_sync()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Verified 1 publication files", result.stdout)

    def test_stale_html_reports_source_mismatch(self):
        (self.root / "dist" / "index.html").write_bytes(b"old version")
        result = self.run_sync()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Canonical HTML source mismatch: dist/index.html", result.stderr)
        self.assertIn("commit the Site source HTML and matching manifest together", result.stderr)


if __name__ == "__main__":
    unittest.main()
