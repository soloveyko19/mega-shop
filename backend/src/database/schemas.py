import pydantic

class ProductBaseSchema(pydantic.BaseModel):
    title: str
    description: str
    price: float
    image_url: str

    class Config:
        orm_mode = True



class ProductOutSchema(ProductBaseSchema):
    id: int

