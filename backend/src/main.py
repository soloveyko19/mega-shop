from fastapi import FastAPI


def init_routes(app: FastAPI):
    from routes.products import router as r1
    from routes.categories import router as r2
    
    app.include_router(r1)
    app.include_router(r2)
    

def create_app():
    app = FastAPI(debug=True)
    init_routes(app)
    
    return app