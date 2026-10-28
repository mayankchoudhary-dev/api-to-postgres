
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from transform import transform_posts


def test_transform_maps_fields():
    posts = [
        {
            "userId": 1,
            "id": 10,
            "title": "  Example title  ",
            "body": "  Example body  ",
        }
    ]

    result = transform_posts(posts)

    assert result == [
        {
            "post_id": 10,
            "user_id": 1,
            "title": "Example title",
            "body": "Example body",
        }
    ]


def test_transform_empty_list():
    assert transform_posts([]) == []
