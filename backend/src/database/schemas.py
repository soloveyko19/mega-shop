from typing import Optional
from pydantic import BaseModel, Field, field_validator, EmailStr
from decimal import Decimal


# Product
class ProductBaseSchema(BaseModel):
    title: str = Field(max_length=100, min_length=3)
    description: str = Field(max_length=4000)
    price: Decimal = Field(decimal_places=2, max_digits=15, ge=0)
    image_url: str 
    category_id: int = Field(ge=0)

    class Config:
        from_attributes = True


class ProductOutSchema(ProductBaseSchema):
    id: int
    owner_id: int


# Category
class CategoryBaseSchema(BaseModel):
    name: str

    class Config:
        from_attributes = True


class CategoryOutSchema(CategoryBaseSchema):
    id: int


# User
class BaseUserSchema(BaseModel):
    email: EmailStr

    class Config:
        from_attributes = True    


class UserInSchema(BaseUserSchema):
    password: str = Field(max_length=100, min_length=8)

    @field_validator("password")
    def password_validator(cls, password: str):
        special_chars = "!@#$%^&*()_+=-{}[]\\|/?.`~"

        for char in password:
            if char in special_chars:
                break
        else:
            raise ValueError("Password should contain at least 1 special character")
        
        for char in password:
            if char.isupper():
              break
        else:
            raise ValueError("Password should contain at least 1 uppercase character")  
        
        for char in password:
            if char.islower():
                break
        else:
            raise ValueError("Password should contain at least 1 lowercase character")
        
        return password



class UserOutSchema(BaseUserSchema):
    id: int
    name: Optional[str] = Field(min_length=3, max_length=100)


class UserUpdateSchema(BaseUserSchema):
    name: str = Field(min_length=3, max_length=100)
    email: EmailStr

