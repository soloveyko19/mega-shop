from typing import List
from fastapi.routing import APIRouter
from database.postgres import Product
from database.schemas import ProductOutSchema, ProductBaseSchema

router = APIRouter()


@router.get("/products")
async def get_products() -> List[ProductOutSchema]:
    products = await Product.all()
    return products


@router.post("/products")
async def post_products(data: ProductBaseSchema) -> ProductOutSchema:
    product = Product(**data.model_dump())
    await product.save()
    return product


