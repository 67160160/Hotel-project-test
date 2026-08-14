from pydantic import BaseModel, Field
from typing import Optional

class ItemBase(BaseModel):
    name: str = Field(..., example="Notebook")
    price: float = Field(..., gt=0, example=25.50)
    description: Optional[str] = Field(None, example="A handy notebook")

class ItemCreate(ItemBase):
    pass

class ItemResponse(ItemBase):
    id: int

    class Config:
        from_attributes = True