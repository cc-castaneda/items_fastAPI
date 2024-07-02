""" 
Módulo que define el servicio para la entidad Item
"""

from app.repositories.item_repository import ItemRepository
from app.schemas.items_schemas import ItemCreate
from sqlalchemy.orm import Session


class ItemsService:
    """
    Servicio para manejar la lógica con Items
    """

    def __init__(self, db: Session):
        self.db = db
        self.repository = ItemRepository(db)

    def create_item(self, item: ItemCreate):
        return self.repository.create(item)

    def get_items(self, skip: int = 0, limit: int = 100):
        return self.repository.get_all(skip, limit)
