from dotenv import find_dotenv, load_dotenv
import os

env_path = find_dotenv()

if not env_path:
    raise FileNotFoundError("File .env not found")

load_dotenv(env_path, override=True)

# General
DOMAIN_NAME = os.environ.get("DOMAIN_NAME")
TESTING = True if os.environ.get("TESTING") == "true" else False 

# Postgres
POSTGRES_HOSTNAME = os.environ.get("POSTGRES_HOSTNAME")
POSTGRES_DB_NAME = os.environ.get("POSTGRES_DB_NAME")
POSTGRES_USERNAME = os.environ.get("POSTGRES_USERNAME")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
