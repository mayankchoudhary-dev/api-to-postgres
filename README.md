
# API to PostgreSQL ETL Pipeline

## Project Overview

This project extracts data from a public REST API, transforms and validates the records using Python, and loads the final data into PostgreSQL.

## Technologies Used

- Python
- REST API
- Requests
- JSON
- Pandas (if used in your implementation)
- PostgreSQL
- Psycopg
- Bash
- Pytest
- Git and GitHub

## Data Source

JSONPlaceholder Posts API:

https://jsonplaceholder.typicode.com/posts

The API normally returns 100 posts containing user IDs, post IDs, titles, and bodies.

## ETL Workflow

1. Extract records from the API.
2. Save the raw response as JSON.
3. Transform the data into a consistent structure.
4. Validate IDs and required fields.
5. Create the PostgreSQL table.
6. Insert or update records in PostgreSQL.
7. Run the workflow using a Python pipeline and Bash script.

## Database Schema

Table: `api_posts`

| Column | Type |
|---|---|
| post_id | INTEGER PRIMARY KEY |
| user_id | INTEGER NOT NULL |
| title | TEXT NOT NULL |
| body | TEXT NOT NULL |

## Project Structure

```text
api-to-postgres/
├── .env.example
├── .gitignore
├── requirements.txt
├── test_api.py
├── transform.py
├── validate.py
├── pipeline.py
├── run_pipeline.sh
├── data/
│   ├── raw/
│   └── processed/
├── logs/
├── sql/
│   └── create_table.sql
├── src/
│   └── load.py
└── tests/
    └── test_transform.py
```

## Setup

1. Clone the repository.
2. Create and activate a Python virtual environment.
3. Install dependencies using `pip install -r requirements.txt`.
4. Create a local `.env` file using `.env.example` as a template.
5. Configure your PostgreSQL connection.
6. Run the pipeline.

## Run the Pipeline

```bash
chmod +x run_pipeline.sh
./run_pipeline.sh
```

## Run Tests

```bash
python -m pytest -v
```

## Verify PostgreSQL Data

```sql
SELECT COUNT(*) FROM api_posts;

SELECT post_id, user_id, title
FROM api_posts
ORDER BY post_id
LIMIT 5;
```

## Key Learning Outcomes

- REST API extraction
- JSON processing
- Data transformation and validation
- PostgreSQL integration
- ETL pipeline automation
- Logging and error handling
- Automated testing
- Bash scripting
