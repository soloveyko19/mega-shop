from dotenv import find_dotenv, load_dotenv
import os

env_path = find_dotenv()

if env_path:
    load_dotenv(env_path, override=True)

# General
TESTING = True if os.environ.get("TESTING", "").lower() == "true" else False 
DOMAIN_NAME = os.environ.get("DOMAIN_NAME", "")

# Postgres
POSTGRES_HOSTNAME = os.environ.get("POSTGRES_HOSTNAME", "")
POSTGRES_DB_NAME = os.environ.get("POSTGRES_DB_NAME", "")
POSTGRES_USER = os.environ.get("POSTGRES_USER", "")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "")

# Redis
REDIS_HOSTNAME = os.environ.get("REDIS_HOSTNAME", "")

# Google OAuth 2.0

GOOGLE_AUTH_CLIENT_ID = os.environ.get("GOOGLE_AUTH_CLIENT_ID", "")
GOOGLE_AUTH_CLIENT_SECRET = os.environ.get("GOOGLE_AUTH_CLIENT_SECRET", "")
GOOGLE_AUTH_REDIRECT_URI = os.environ.get("GOOGLE_AUTH_REDIRECT_URI", "")
