
import json
from pathlib import Path

INPUT_FILE = Path("data/raw/posts.json")
OUTPUT_FILE = Path("data/processed/posts_clean.json")


def transform_posts(posts):
    cleaned_posts = []

    for post in posts:
        cleaned_post = {
            "post_id": post["id"],
            "user_id": post["userId"],
            "title": post["title"].strip(),
            "body": post["body"].strip(),
        }

        cleaned_posts.append(cleaned_post)

    return cleaned_posts


def main():
    with INPUT_FILE.open("r", encoding="utf-8") as file:
        posts = json.load(file)

    cleaned_posts = transform_posts(posts)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with OUTPUT_FILE.open("w", encoding="utf-8") as file:
        json.dump(cleaned_posts, file, indent=2, ensure_ascii=False)

    print("Raw records:", len(posts))
    print("Transformed records:", len(cleaned_posts))
    print("Saved to:", OUTPUT_FILE)
    print("First transformed record:", cleaned_posts[0])


if __name__ == "__main__":
    main()
