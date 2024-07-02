"""
 Módulo que define las rutas de la API para la entidad Item
 """

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.items_schemas import Item, ItemCreate
from app.services.items_service import ItemsService
from app.database import get_db

router = APIRouter()


def get_items_service(db: Session = Depends(get_db)):
    """
    Como dependencia para obtener una instancia del servicio de Items
    """
    return ItemsService(db)


@router.post("/items/", response_model=Item)
def create_item(item: ItemCreate, service: ItemsService = Depends(get_items_service)):
    return service.create_item(item)


@router.get("/items/", response_model=List[Item])
def list_items(
    skip: int = 0, limit: int = 100, service: ItemsService = Depends(get_items_service)
):
    return service.get_items(skip=skip, limit=limit)
