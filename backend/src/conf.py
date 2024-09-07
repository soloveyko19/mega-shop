from dotenv import load_dotenv, get_key

if not load_dotenv():
    raise FileNotFoundError("File .env not found")

POSTGRES_HOSTNAME = get_key("POSTGRES_HOSTNAME")
POSTGRES_USERNAME = get_key("POSTGRES_USERNAME")
POSTGRES_PASSWORD = get_key("POSTGRES_PASSWORD")
