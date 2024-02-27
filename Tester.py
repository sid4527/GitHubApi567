import unittest
from unittest.mock import Mock, patch
from assignment_Part_one import get_user_repositories  


class TestGetUserRepositories(unittest.TestCase):

    @patch('requests.get')
    def test_get_user_repositories_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{'name': 'repo1'}, {'name': 'repo2'}]

        repos_with_commits = get_user_repositories('test_user')
        self.assertIsNotNone(repos_with_commits)
        self.assertEqual(len(repos_with_commits), 2)

    @patch('requests.get')
    def test_get_user_repositories_failed_request(self, mock_get):
        mock_get.return_value.status_code = 404

        repos_with_commits = get_user_repositories('test_user')
        self.assertIsNone(repos_with_commits)

    @patch('requests.get')
    def test_get_user_repositories_failed_commits_request(self, mock_get):
        mock_get.side_effect = [
            Mock(status_code=200, json=lambda: [{'name': 'repo1'}]),
            Mock(status_code=404)
        ]

        repos_with_commits = get_user_repositories('test_user')
        self.assertIsNotNone(repos_with_commits)
        self.assertEqual(len(repos_with_commits), 0)


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)