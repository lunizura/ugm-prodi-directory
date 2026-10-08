## Summary of Changes

<!-- Provide a concise explanation of what changes were made and why. -->

## Related Issues

<!-- Link any relevant issues resolved by this PR (e.g. Closes #12). -->
Closes #

## Type of Change

- [ ] Data Correction (fixing outdated quota, accreditation, or curriculum)
- [ ] New Feature (adding UI components, filters, or analytical views)
- [ ] Performance & Refactor (improving client-side script or layout responsiveness)
- [ ] Documentation (updating README, guides, or specifications)
- [ ] Test Suite (adding test cases or assertions)

## Pre-Merge Verification Checklist

Please verify and check all applicable items before requesting review:

- [ ] Automated test suite executed locally and passes 100%:
  ```bash
  python -m unittest tests/test_ugm_directory.py -v
  ```
- [ ] Mathematical quota parity holds for all modified programs:
  `daya_tampung == dt_snbp + dt_snbt + dt_umugm`
- [ ] Bilingual completeness verified (complete ID and EN text for all qualitative fields).
- [ ] Official reference source URL cited in PR or issue description.
- [ ] Strict zero-emoji policy maintained across all modified lines and commit messages.
