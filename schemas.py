from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    price: float

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class config:
        orm_mode = True