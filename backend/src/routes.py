from fastapi.routing import APIRouter

router = APIRouter()


@router.get("/products")
async def get_products():
    return []