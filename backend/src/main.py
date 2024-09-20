from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

import conf


def init_routes(app: FastAPI):
    from routes.products import router as r1
    from routes.categories import router as r2
    from routes.users import router as r3
    
    app.include_router(r1)
    app.include_router(r2)
    app.include_router(r3)


def setup_cors(app: FastAPI):
    origins = [
        conf.DOMAIN_NAME
    ]
    methods = (
        "GET",
        "POST",
        "PUT"
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_methods=methods,
        allow_credentials=True
    )

def setup_middlewares(app: FastAPI):
    from middlewares.auth_middleware import AuthMiddleware
    app.add_middleware(BaseHTTPMiddleware, dispatch=AuthMiddleware())


def load_config(app: FastAPI):
    init_routes(app)
    setup_cors(app)
    setup_middlewares(app)

    app.root_path =  "/api"


def create_app():
    app = FastAPI(debug=True)

    load_config(app)
    
    return app