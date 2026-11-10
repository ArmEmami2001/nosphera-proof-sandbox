# UAT 10 Nov fixture note

1. This fixture note records a harmless UAT run dated 10 Nov.
2. Fixtures are sample data used to put tests into a known state.
3. Each fixture should be small, predictable, and easy to read.
4. Keep fixture values stable so test results stay repeatable.
5. Name fixtures clearly so their purpose is obvious at a glance.
6. Avoid real personal data in fixtures; use made-up placeholders.
7. Reset fixtures between runs to prevent state from leaking.
8. Store fixtures near the tests that rely on them.
9. Document any assumptions a fixture bakes in.
10. Prefer the smallest fixture that still exercises the case.
11. Review fixtures when the schema they mirror changes.
12. Remove stale fixtures once their tests are retired.
