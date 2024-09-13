import secrets


async def generate_session_id():
    return secrets.token_urlsafe(32)
