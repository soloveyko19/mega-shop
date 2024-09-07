import pydantic

class ProductBaseSchema(pydantic.BaseModel):
    title: str
    description: str
    price: float
    image_url: str

    class Config:
        from_attributes = True



class ProductOutSchema(ProductBaseSchema):
    id: int

