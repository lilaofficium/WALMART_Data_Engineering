
import os
from pathlib import Path

import psycopg2
from dotenv import load_dotenv
# append the project root to sys.path to allow imports from src
PROJECT_ROOT = Path(__file__).resolve().parents[2]
append_path = str(PROJECT_ROOT)
if append_path not in os.sys.path:
    os.sys.path.append(append_path)
from src.utils.logger import get_logger
# from src.utils.paths import ENV_FILE

logger = get_logger(__name__)

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("NEON_HOST"),
    "port": os.getenv("NEON_PORT"),
    "database": os.getenv("NEON_DBNAME"),
    "user": os.getenv("NEON_USER"),
    "password": os.getenv("NEON_PASSWORD"),
}


def get_connection(): 
    try:
        connection = psycopg2.connect(**DB_CONFIG)
        logger.info("PostgreSQL connection successful.")
        return connection
    except Exception:
        logger.exception("PostgreSQL connection failed.")
        return None


def test_connection() -> bool: 
    connection = None
    try:
        connection = psycopg2.connect(**DB_CONFIG)
        logger.info("PostgreSQL connection successful.")
        return True
    except Exception:
        logger.exception("PostgreSQL connection failed.")
        return False
    finally:
        if connection:
            connection.close()
 
if __name__ == "__main__":
    if test_connection():
        logger.info("Database connection test passed.")
    else:
        logger.error("Database connection test failed.")