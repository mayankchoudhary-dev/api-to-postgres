
import logging
import subprocess
import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent
LOG_DIR = PROJECT_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_DIR / "pipeline.log"),
        logging.StreamHandler(),
    ],
)

STEPS = [
    ["test_api.py"],
    ["transform.py"],
    ["validate.py"],
    ["src/load.py"],
]


def run_pipeline():
    for step in STEPS:
        command = [sys.executable, *step]
        logging.info("Starting: %s", " ".join(step))

        try:
            subprocess.run(
                command,
                cwd=PROJECT_DIR,
                check=True,
            )
            logging.info("Completed: %s", " ".join(step))
        except subprocess.CalledProcessError:
            logging.exception("Pipeline failed at: %s", " ".join(step))
            raise

    logging.info("ETL pipeline completed successfully.")


if __name__ == "__main__":
    run_pipeline()
