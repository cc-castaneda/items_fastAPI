from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class ItemBase(BaseModel):
    """
    Base para Item
    """

    name: str
    price: float


class ItemCreate(ItemBase):
    pass


class ItemUpdate(BaseModel):
    """
    Esquema para actualizar un Item existente
    """

    name: Optional[str] = None
    price: Optional[float] = None


class Item(ItemBase):
    """
    Esquema completo de Item para respuestas de API
    """

    id: int
    created_at: datetime
    updated_at: Optional[datetime] = Field(default_factory=datetime.now)

    class Config:
        orm_mode = True
