from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def init_routes(app: FastAPI):
    from routes.products import router as r1
    from routes.categories import router as r2
    from routes.users import router as r3
    
    app.include_router(r1)
    app.include_router(r2)
    app.include_router(r3)


def setup_cors(app: FastAPI):
    origins = [
        "*"
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
    )


def config_app(app: FastAPI):
    init_routes(app)
    setup_cors(app)


def create_app():
    app = FastAPI(debug=True)

    config_app(app)
    
    return app