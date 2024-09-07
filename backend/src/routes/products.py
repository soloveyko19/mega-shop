from typing import Iterable, List
from fastapi.routing import APIRouter
from database.postgres import Product
from database.schemas import ProductOutSchema, ProductBaseSchema

router = APIRouter()


@router.get("/products", response_model=List[ProductOutSchema])
async def get_products() -> Iterable[Product]:
    products = await Product.all()
    return products


@router.post("/products", response_model=ProductOutSchema)
async def post_products(data: ProductBaseSchema) -> Product:
    product = Product(**data.model_dump())
    await product.save()
    return product


