from unittest.mock import patch
import pytest
from services.comment import register_comment, get_all_comments
from models.comment import Comment
from models.user import User


class MockComment:
    def __init__(self, id, content, created_at, external_name, posted_by, user, asset_id):
        self.id = id
        self.content = content
        self.created_at = created_at
        self.external_name = external_name
        self.posted_by = posted_by
        self.user = user
        self.asset_id = asset_id


class MockUser:
    def __init__(self, fullname):
        self.fullname = fullname


def mock_query(asset_id):
    # Create mock comment data for testing
    mock_comments = [
        MockComment(1, "Test comment 1", "2023-08-05", "External", 1, MockUser("John Doe"), asset_id),
        MockComment(2, "Test comment 2", "2023-08-05", "External", 2, MockUser("Jane Smith"), asset_id),
    ]
    return mock_comments


def test_get_all_comments():
    # Test with a list of comments
    with patch('models.comment.Comment.get_all_by', side_effect=mock_query):
        asset_id = 1  # Replace with the desired asset_id for testing
        expected_result = {
            'comments': mock_query(asset_id)
        }

        # Call the function and assert the result
        result, status_code = get_all_comments(asset_id)
        assert status_code == 200
        assert len(result['comments']) == len(expected_result['comments'])

