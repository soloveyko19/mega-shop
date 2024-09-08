from typing import Iterable, List

from fastapi.routing import APIRouter
from fastapi.exceptions import HTTPException

from database.postgres import Category, Product
from database.schemas import ProductOutSchema, ProductInSchema

router = APIRouter()


@router.get("/products", response_model=List[ProductOutSchema])
async def get_products() -> Iterable[Product]:
    products = await Product.all()
    return products


@router.post("/products", response_model=ProductOutSchema, status_code=201)
async def post_products(data: ProductInSchema) -> Product:
    product = Product(**data.model_dump())
    await product.save()
    return product


@router.get("/products/category/{category_id}", response_model=List[ProductOutSchema])
async def get_products_by_category(category_id: int) -> Iterable[Product]:
    category = await Category.get(category_id)
    if not category:
        raise HTTPException(404, "Oops... Looks like you're requesting a category that doesn't exist.")
    products = category.products
    return products


@router.get("/products/{id}", response_model=ProductOutSchema)
async def get_product_by_id(id: int):
    product = await Product.get(id)
    if not product:
        raise HTTPException(404, "Oops... Looks like you're requesting a product that doesn't exist.")
    return product


@router.put("/products/{id}", response_model=ProductOutSchema)
async def put_product_by_id(new_product: ProductInSchema, id: int):
    product = await Product.get(id)
    if not product:
        raise HTTPException(404, "No such product you're requesting.")
    for field, value in new_product.model_dump().items():
        product.__setattr__(field, value)
    await product.save()
    return product
