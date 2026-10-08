# Contributing to UGM Study Programs Directory

Thank you for your interest in contributing to the Universitas Gadjah Mada (UGM) Study Programs and Accreditation Directory. This project aims to provide transparent, accurate, and accessible educational data for prospective students, researchers, and academic counselors.

To maintain dataset integrity, reliability, and code quality, please adhere to the following contribution guidelines.

---

## Code of Conduct

We are committed to providing a welcoming, productive, and harassment-free environment. All contributors and participants are expected to maintain professional, constructive, and respectful communication in all issues, discussions, and pull requests.

---

## Ways to Contribute

1. **Reporting Data Corrections:** Report outdated daya tampung, changes in national (BAN-PT/LAM) or international accreditations, or missing study programs.
2. **Proposing Feature Enhancements:** Suggest UI improvements, new filter categories, analytical visualizations, or export options.
3. **Submitting Code Changes:** Fix bugs, optimize client-side rendering performance, or enhance mobile accessibility.

---

## Local Development Workflow

### 1. Prerequisites
- Python 3.9 or higher (no external third-party dependencies required; standard library only).
- A modern web browser (Chrome, Firefox, Safari, or Edge).
- Git installed and configured.

### 2. Setup
Clone the repository and inspect the directory structure:
```bash
git clone https://github.com/lunizura/ugm-prodi-directory.git
cd ugm-prodi-directory
```

### 3. File Organization
- `data/ugm_prodi.json`: Raw structured dataset of all 74 study programs.
- `data/ugm_prodi.js`: Client-ready JavaScript data bundle for the static interface.
- `data/ugm_prodi.csv`: Tabular CSV export.
- `data/metadata.json`: Dataset metadata, totals, and verification metrics.
- `index.html`: Responsive bilingual web directory application.
- `scripts/build_ugm_dataset.py`: Generator script for dataset compilation and quota balancing.
- `tests/test_ugm_directory.py`: Automated end-to-end regression validation suite.

---

## Data Verification & Mathematical Parity

If you submit changes to the dataset, your edits must satisfy the following strict rules:

1. **Mathematical Quota Equality:**
   For every study program, the total seat allocation must strictly equal the sum of its admission tracks:
   ```
   daya_tampung == dt_snbp + dt_snbt + dt_umugm
   ```
2. **Bilingual Parity:**
   Every study program entry must provide complete content in both Bahasa Indonesia and English (`deskripsi`, `fokus`, and `karir`).
3. **Official Sourcing:**
   All quota and accreditation changes must be accompanied by an official verification reference (e.g. `um.ugm.ac.id`, BAN-PT, or LAM announcements).

---

## Running the Automated Test Suite

Before committing or pushing any changes, execute the test suite locally:
```bash
python -m unittest tests/test_ugm_directory.py -v
```
All 9 tests must pass with 100% success rate (`OK`).

---

## Strict Zero-Emoji Policy

This repository strictly enforces a zero-emoji policy across all files, code, comments, commit messages, issue templates, and documentation. Automated test suites will fail if any emoji codepoint is detected.

---

## Commit Message Guidelines

We follow Conventional Commits formatting:
- `feat:` for new features or substantial additions
- `fix:` for bug fixes or data corrections
- `docs:` for documentation updates
- `test:` for test additions or modifications
- `chore:` for repository maintenance or workflow updates

Example:
```
feat: add sub-quota breakdown for international undergraduate program
```

---

## Pull Request Process

1. Create a descriptive branch from `main`:
   ```bash
   git checkout -b fix/correct-farmasi-accreditation
   ```
2. Make your atomic changes and verify tests locally.
3. Push your branch to GitHub and open a Pull Request using the repository template.
4. Ensure your PR description references the relevant issue (e.g. `Closes #4`).
