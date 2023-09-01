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
        """Test the org method returns expected result"""
        mocked_function.return_value = MagicMock(return_value=response)
        gh_org_client = GithubOrgClient(org)
        self.assertEqual(gh_org_client.org(), response)
        mocked_function.assert_called_once_with(
                "https://api.github.com/orgs/{}".format(org))


    def test_public_repos_url(self) -> None:
        """Test the _public_repos_url instance method"""
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos"
            )


if __name__ == "__main__":
    unittest.main()
