import unittest

from proof_fixture import pull_request_parts


class PullRequestPartsTest(unittest.TestCase):
    def test_canonical_reference(self):
        self.assertEqual(
            pull_request_parts("https://github.com/example/sample/pull/42"),
            ("example", "sample", 42),
        )

    def test_rejects_issue_and_query(self):
        for link in (
            "https://github.com/example/sample/issues/42",
            "https://github.com/example/sample/pull/42?source=example",
            "https://other.example/example/sample/pull/42",
        ):
            with self.subTest(link=link), self.assertRaises(ValueError):
                pull_request_parts(link)
