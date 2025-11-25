from pydantic import BaseModel

class ProductSchema(BaseModel):
    title: str
    price: str
    availability: str
    category: str
    rating: str
    product_url: str

    class Config:
        orm_mode = True
