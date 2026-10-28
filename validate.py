
import json
from pathlib import Path

INPUT_FILE = Path("data/processed/posts_clean.json")


def validate_posts(posts):
    errors = []
    seen_ids = set()

    for index, post in enumerate(posts, start=1):
        post_id = post.get("post_id")
        user_id = post.get("user_id")
        title = post.get("title")
        body = post.get("body")

        if not isinstance(post_id, int) or isinstance(post_id, bool) or post_id <= 0:
            errors.append(f"Record {index}: invalid post_id")

        elif post_id in seen_ids:
            errors.append(f"Record {index}: duplicate post_id {post_id}")

        else:
            seen_ids.add(post_id)

        if not isinstance(user_id, int) or isinstance(user_id, bool) or user_id <= 0:
            errors.append(f"Record {index}: invalid user_id")

        if not isinstance(title, str) or not title.strip():
            errors.append(f"Record {index}: missing or invalid title")

        if not isinstance(body, str) or not body.strip():
            errors.append(f"Record {index}: missing or invalid body")

    return errors


def main():
    with INPUT_FILE.open("r", encoding="utf-8") as file:
        posts = json.load(file)

    if not isinstance(posts, list):
        raise ValueError("Expected a list of records")

    errors = validate_posts(posts)

    print("Records checked:", len(posts))
    print("Validation errors:", len(errors))

    for error in errors:
        print("-", error)

    if errors:
        raise SystemExit("Validation failed")

    print("Validation passed!")


if __name__ == "__main__":
    main()
