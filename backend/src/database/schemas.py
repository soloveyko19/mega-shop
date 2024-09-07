from pydantic import BaseModel

class ProductBaseSchema(BaseModel):
    title: str
    description: str
    price: float
    image_url: str
    category_id: int | None

    class Config:
        from_attributes = True


class ProductInSchema(BaseModel):
    category_id: int


class ProductOutSchema(ProductBaseSchema):
    id: int


class CategoryBaseSchema(BaseModel):
    name: str

    class Config:
        from_attributes = True


class CategoryOutSchema(CategoryBaseSchema):
    id: int
