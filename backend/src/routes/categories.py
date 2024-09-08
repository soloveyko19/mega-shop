from typing import List, Iterable
from fastapi import APIRouter, HTTPException
from database.postgres import Category
from database.schemas import CategoryOutSchema, CategoryBaseSchema

router = APIRouter()


@router.get("/category", response_model=List[CategoryOutSchema])
async def get_category_list() -> Iterable[Category]:
    categories = await Category.all()
    return categories


@router.post("/category", response_model=CategoryOutSchema, status_code=201)
async def post_category(data: CategoryBaseSchema) -> Category:
    category = Category(**data.model_dump())
    await category.save()
    return category

@router.get("/category/{id}", response_model=CategoryOutSchema)
async def get_category_by_id(id: int) -> Category:
    category = await Category.get(id)
    if not category:
        raise HTTPException(404, "Oops... Looks like you're requesting a category that doesn't exist.")
    return category
    
