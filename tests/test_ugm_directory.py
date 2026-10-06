"""
Automated end-to-end validation test suite for Universitas Gadjah Mada (UGM) Study Programs Directory.
Verifies dataset integrity across JSON, JS, CSV, and metadata, admission quota mathematical parity,
DOM element contract obligations in index.html, bilingual data completeness, and strict zero-emoji compliance.
"""

import os
import json
import csv
import re
import unittest

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT_DIR, "data")
INDEX_HTML = os.path.join(ROOT_DIR, "index.html")
README_MD = os.path.join(ROOT_DIR, "README.md")


class TestDatasetIntegrity(unittest.TestCase):
    """Verify integrity, counts, and parity across UGM data files."""

    @classmethod
    def setUpClass(cls):
        with open(os.path.join(DATA_DIR, "metadata.json"), "r", encoding="utf-8") as f:
            cls.metadata = json.load(f)

        with open(os.path.join(DATA_DIR, "ugm_prodi.json"), "r", encoding="utf-8") as f:
            cls.prodi_json = json.load(f)

        with open(os.path.join(DATA_DIR, "ugm_prodi.js"), "r", encoding="utf-8") as f:
            content = f.read()
            match_data = re.search(r"window\.UGM_PRODI_DATA\s*=\s*(\[[\s\S]*?\]);", content)
            assert match_data is not None, "ugm_prodi.js must define window.UGM_PRODI_DATA"
            cls.prodi_js = json.loads(match_data.group(1))

            match_fac = re.search(r"window\.UGM_FACULTIES\s*=\s*(\{[\s\S]*?\});", content)
            assert match_fac is not None, "ugm_prodi.js must define window.UGM_FACULTIES"
            cls.faculties_js = json.loads(match_fac.group(1))

        with open(os.path.join(DATA_DIR, "ugm_prodi.csv"), "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            cls.prodi_csv = list(reader)

    def test_total_counts(self):
        """Verify program counts across metadata, JSON, JS, and CSV."""
        expected_total = 74
        self.assertEqual(self.metadata["total_prodi"], expected_total)
        self.assertEqual(len(self.prodi_json), expected_total)
        self.assertEqual(len(self.prodi_js), expected_total)
        self.assertEqual(len(self.prodi_csv), expected_total)
        self.assertEqual(self.metadata["total_fakultas"], 19)
        self.assertEqual(len(self.faculties_js), 19)
        self.assertEqual(self.metadata["total_s1"], 62)
        self.assertEqual(self.metadata["total_vokasi_d4"], 10)
        self.assertEqual(self.metadata["total_pascasarjana"], 2)
        self.assertEqual(self.metadata["total_unggul"], expected_total)
        self.assertEqual(self.metadata["total_akreditasi_internasional"], 58)
        self.assertEqual(self.metadata["total_daya_tampung"], 8200)

    def test_faculty_coverage(self):
        """Ensure all 18 UGM faculties and Sekolah Vokasi are represented."""
        expected_faculties = {
            "Biologi", "FEB", "Farmasi", "Filsafat", "Geografi",
            "FH", "FIB", "FISIPOL", "FKG", "FKH",
            "FK-KMK", "Kehutanan", "FMIPA", "Pertanian",
            "Peternakan", "FPsi", "FT", "FTP", "SV"
        }
        json_faculties = {p["fakultas_singkatan"] for p in self.prodi_json}
        self.assertEqual(json_faculties, expected_faculties)
        self.assertEqual(set(self.faculties_js.keys()), expected_faculties)

    def test_unique_identifiers(self):
        """Ensure prodi IDs and codes are strictly unique."""
        ids = [p["id"] for p in self.prodi_json]
        self.assertEqual(len(ids), len(set(ids)), "Prodi IDs must be strictly unique")

        codes = [p["kode"] for p in self.prodi_json]
        self.assertEqual(len(codes), len(set(codes)), "Prodi codes must be strictly unique")


class TestQuotaBalance(unittest.TestCase):
    """Verify strict mathematical parity for admission quota allocations."""

    @classmethod
    def setUpClass(cls):
        with open(os.path.join(DATA_DIR, "ugm_prodi.json"), "r", encoding="utf-8") as f:
            cls.prodi_json = json.load(f)

    def test_quota_equality(self):
        """Ensure daya_tampung == dt_snbp + dt_snbt + dt_umugm for every program."""
        mismatches = []
        for p in self.prodi_json:
            total = p["daya_tampung"]
            components_sum = p["dt_snbp"] + p["dt_snbt"] + p["dt_umugm"]
            if total != components_sum:
                mismatches.append(f"{p['id']}: total={total} vs sum={components_sum}")

        self.assertEqual(mismatches, [], f"Quota balance violations found: {mismatches}")

    def test_non_negative_quotas(self):
        """Ensure no quota value is negative."""
        for p in self.prodi_json:
            self.assertGreaterEqual(p["daya_tampung"], 0)
            self.assertGreaterEqual(p["dt_snbp"], 0)
            self.assertGreaterEqual(p["dt_snbt"], 0)
            self.assertGreaterEqual(p["dt_umugm"], 0)


class TestDOMContract(unittest.TestCase):
    """Verify that index.html contains all expected DOM elements and attributes."""

    @classmethod
    def setUpClass(cls):
        with open(INDEX_HTML, "r", encoding="utf-8") as f:
            cls.html_content = f.read()

    def test_critical_dom_ids(self):
        """Verify presence of all mandatory DOM IDs in the directory interface."""
        expected_ids = [
            "search-input",
            "filter-jenjang",
            "filter-fakultas",
            "filter-rumpun",
            "filter-akreditasi-intl",
            "btn-reset-filters",
            "prodi-grid",
            "prodi-table-container",
            "prodi-table-body",
            "results-count",
            "empty-state",
            "btn-toggle-lang",
            "lang-indicator",
            "view-mode-grid",
            "view-mode-table",
            "modal-backdrop",
            "modal-card",
            "modal-close",
            "modal-title",
            "modal-title-en",
            "modal-faculty",
            "modal-quota-total",
            "modal-quota-snbp",
            "modal-quota-snbt",
            "modal-quota-um",
            "modal-um-desc",
            "modal-desc",
            "modal-fokus-container",
            "modal-karir-container",
            "modal-ukt-text",
            "modal-link-official",
            "modal-btn-share",
            "modal-btn-close",
            "toast-msg"
        ]
        for element_id in expected_ids:
            self.assertIn(f'id="{element_id}"', self.html_content, f"Missing DOM ID: {element_id}")

    def test_meta_and_viewport(self):
        """Verify SEO and responsive meta tags."""
        self.assertIn('<meta name="viewport"', self.html_content)
        self.assertIn('<meta charset="UTF-8"', self.html_content)
        self.assertIn("UGM", self.html_content)


class TestBilingualParity(unittest.TestCase):
    """Verify that all programs provide Indonesian and English content."""

    @classmethod
    def setUpClass(cls):
        with open(os.path.join(DATA_DIR, "ugm_prodi.json"), "r", encoding="utf-8") as f:
            cls.prodi_json = json.load(f)

    def test_bilingual_fields(self):
        """Ensure nama_en, deskripsi (id/en), fokus (id/en), and karir (id/en) exist."""
        for p in self.prodi_json:
            self.assertTrue(len(p.get("nama_en", "").strip()) > 0, f"Missing nama_en in {p['id']}")
            self.assertIn("id", p["deskripsi"])
            self.assertIn("en", p["deskripsi"])
            self.assertTrue(len(p["deskripsi"]["id"].strip()) > 0)
            self.assertTrue(len(p["deskripsi"]["en"].strip()) > 0)

            self.assertIn("id", p["fokus"])
            self.assertIn("en", p["fokus"])
            self.assertTrue(len(p["fokus"]["id"]) >= 2)
            self.assertTrue(len(p["fokus"]["en"]) >= 2)

            self.assertIn("id", p["karir"])
            self.assertIn("en", p["karir"])
            self.assertTrue(len(p["karir"]["id"]) >= 2)
            self.assertTrue(len(p["karir"]["en"]) >= 2)


class TestZeroEmojiCompliance(unittest.TestCase):
    """Strictly assert that no emojis exist in repository code, data, markup, or docs."""

    def test_no_emojis_in_repository(self):
        """Scan all repository text files and assert zero emoji codepoints."""
        emoji_violations = []

        for root, dirs, files in os.walk(ROOT_DIR):
            if ".git" in dirs:
                dirs.remove(".git")
            for filename in files:
                file_path = os.path.join(root, filename)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                except (UnicodeDecodeError, PermissionError):
                    continue

                for line_num, line in enumerate(content.splitlines(), start=1):
                    for ch in line:
                        code = ord(ch)
                        # Check Unicode blocks for emojis and pictographs
                        if code > 127 and (
                            0x1F300 <= code <= 0x1FAFF or
                            0x2600 <= code <= 0x27BF or
                            0x1F1E6 <= code <= 0x1F1FF
                        ):
                            rel_path = os.path.relpath(file_path, ROOT_DIR)
                            emoji_violations.append(
                                f"{rel_path}:{line_num} contains emoji U+{code:04X} ('{ch}')"
                            )

        self.assertEqual(
            emoji_violations,
            [],
            f"Zero emoji policy violated! Found {len(emoji_violations)} emojis:\n" +
            "\n".join(emoji_violations[:10])
        )


if __name__ == "__main__":
    unittest.main()
