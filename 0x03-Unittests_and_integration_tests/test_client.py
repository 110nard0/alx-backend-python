#!/usr/bin/env python3
"""test_client module"""

import unittest
from client import GithubOrgClient
from parameterized import parameterized
from typing import Dict
from unittest.mock import MagicMock, Mock, patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """Inherits from unittest TestCase class and tests GithubOrgClient class"""
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch("client.get_json")
    def test_org(self, org: str, response: Dict,
                 mocked_function: MagicMock) -> None:
        mocked_function.return_value = MagicMock(return_value=response)
        gh_org_client = GithubOrgClient(org)
        self.assertEqual(gh_org_client.org(), response)
        mocked_function.assert_called_once_with(
                "https://api.github.com/orgs/{}".format(org))


if __name__ == "__main__":
    unittest.main()
