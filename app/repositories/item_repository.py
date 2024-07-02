from sqlalchemy.orm import Session
from app.models.items import Item
from app.schemas.items_schemas import ItemCreate
from datetime import datetime


class ItemRepository:
    """
    Como repositorio para manejar operaciones de base de datos relacionadas con Items
    """

    def __init__(self, db: Session):
        self.db = db

    def create(self, item: ItemCreate):
        db_item = Item(
            **item.model_dump(), created_at=datetime.now(), updated_at=datetime.now()
        )
        self.db.add(db_item)
        self.db.commit()
        self.db.refresh(db_item)
        return db_item

    def get_all(self, skip: int = 0, limit: int = 100):
        return self.db.query(Item).offset(skip).limit(limit).all()
