#!/usr/bin/env python3
"""
test_clinet.py tests"""
import unittest
from unittest.mock import patch, MagicMock, PropertyMock
from parameterized import parameterized, parameterized_class
from typing import Dict, List

import client
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Simple tests"""
    @parameterized.expand(["org1", "org2"])
    @patch('client.get_json')
    def test_org(
        self, organization: str, mock_get_json: MagicMock
    ) -> None:
        """Org property test"""
        git_client = GithubOrgClient(organization)
        self.assertEqual(git_client.org, mock_get_json.return_value)
        mock_get_json.assert_called_once_with(
            git_client.ORG_URL.format(org=organization)
        )

    def test_public_repos_url(self) -> None:
        """Repo URL test"""
        config = {
            'return_value.repos_url': 'https://api.github.com/test/repos/alx'
        }
        with patch(
            'client.GithubOrgClient.org',
            new_callable=PropertyMock, **config
        ) as mock_org:
            test = GithubOrgClient('test')
            self.assertEqual(
                test._public_repos_url,
                mock_org.return_value['repos_url']
            )

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """Repo list test"""
        mock_get_json.return_value = [
            {'name': 'repo1', 'license': {'key': 'lic1'}},
            {'name': 'repo2', 'license': {'key': 'lic2'}},
            {'name': 'repo3', 'license': {'key': 'lic1'}}
        ]
        prop_value = {
            'return_value': 'https://api.github.com/orgs/test/repos'
        }
        with patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock, **prop_value
        ) as mock_public_repo:
            test = GithubOrgClient('test')
            self.assertEqual(
                test.public_repos(), ['repo1', 'repo2', 'repo3']
            )
            mock_public_repo.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "key1"}}, "key1", True),
        ({"license": {"key": "key2"}}, "key1", False),
    ])
    def test_has_license(self, license_info: Dict, key: str, expected: bool) -> None:
        """License check test"""
        self.assertEqual(
            GithubOrgClient.has_license(license_info, key), expected
        )


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'), TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """GithubOrgClient Integration test"""
    @classmethod
    def setUpClass(cls) -> None:
        """SetUp Class"""
        def response(url):
            """Mocks request.get(url).json()"""
            config = {'json.return_value': []}
            for payload in TEST_PAYLOAD:
                if url == payload[0]['repos_url']:
                    config = {'json.return_value': payload[1]}
                    break
            return MagicMock(**config)

        cls.get_patcher = patch('requests.get', side_effect=response)
        cls.org_patcher = patch(
            'client.GithubOrgClient.org',
            new_callable=PropertyMock, **{'return_value': cls.org_payload}
        )
        cls.get_patcher.start()
        cls.org_patcher.start()

    def test_public_repos(self) -> None:
        """Public repos test"""
        test = GithubOrgClient('test/repos')
        self.assertEqual(
            self.expected_repos,
            test.public_repos(license=None)
        )

    def test_public_repos_with_license(self) -> None:
        """Public repos with license test"""
        test = GithubOrgClient('test/repos')
        self.assertEqual(
            self.apache2_repos,
            test.public_repos(license="apache-2.0")
        )

    @classmethod
    def tearDownClass(cls) -> None:
        """TearDown Class"""
        cls.get_patcher.stop()
        cls.org_patcher.stop()
