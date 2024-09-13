from fastapi import FastAPI, Request, Response
from fastapi.middleware import Middleware
from starlette.middleware import _MiddlewareClass
from starlette.types import ASGIApp


from database.redis import session_storage
from database.postgres import User


class AuthMiddleware:
    def __init__(self) -> None:
        pass

    async def __call__(self, request: Request, call_next) -> Response:
        session_id = request.cookies.get("session_id")
        request.state.user = None
        request.state.session_id = None
        if session_id:
            request.state.session_id = session_id
            encoded_username = await session_storage.get(session_id)
            if encoded_username:
                username = encoded_username.decode()
                user = await User.get_by_username(username)
                request.state.user = user
                
        return await call_next(request)

