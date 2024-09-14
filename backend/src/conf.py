from dotenv import find_dotenv, load_dotenv
import os

env_path = find_dotenv()

if env_path:
    load_dotenv(env_path, override=True)

# General
TESTING = True if os.environ.get("TESTING", "").lower() == "true" else False 

# Postgres
POSTGRES_HOSTNAME = os.environ.get("POSTGRES_HOSTNAME", "")
POSTGRES_DB_NAME = os.environ.get("POSTGRES_DB_NAME", "")
POSTGRES_USER= os.environ.get("POSTGRES_USER", "")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "")

# Redis
REDIS_HOSTNAME = os.environ.get("REDIS_HOSTNAME", "")
