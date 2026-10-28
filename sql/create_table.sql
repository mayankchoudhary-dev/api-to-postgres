
CREATE TABLE IF NOT EXISTS api_posts (
    post_id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    body TEXT NOT NULL
);

