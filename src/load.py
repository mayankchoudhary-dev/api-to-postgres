
import json
import os
from pathlib import Path

import psycopg
from dotenv import load_dotenv

load_dotenv()

INPUT_FILE = Path("data/processed/posts_clean.json")
SQL_FILE = Path("sql/create_table.sql")


def load_posts():
    with INPUT_FILE.open("r", encoding="utf-8") as file:
        posts = json.load(file)

    if not posts:
        print("No records to load.")
        return

    create_table_sql = SQL_FILE.read_text(encoding="utf-8")

    db_config = {
        "host": os.environ["DB_HOST"],
        "port": os.environ.get("DB_PORT", "5432"),
        "dbname": os.environ["DB_NAME"],
        "user": os.environ["DB_USER"],
        "password": os.environ["DB_PASSWORD"],
    }

    with psycopg.connect(**db_config) as conn:
        with conn.cursor() as cur:
            cur.execute(create_table_sql)

            cur.executemany(
                """
                INSERT INTO api_posts (post_id, user_id, title, body)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (post_id) DO UPDATE SET
                    user_id = EXCLUDED.user_id,
                    title = EXCLUDED.title,
                    body = EXCLUDED.body
                """,
                [
                    (
                        post["post_id"],
                        post["user_id"],
                        post["title"],
                        post["body"],
                    )
                    for post in posts
                ],
            )

    print("Records processed:", len(posts))
    print("Data loaded into api_posts successfully.")


if __name__ == "__main__":
    load_posts()
