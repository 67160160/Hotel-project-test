from sqlalchemy.orm import Session
from app.models.item import ItemModel
from app.schemas.item import ItemCreate

def get_item_by_id(db: Session, item_id: int):
    return db.query(ItemModel).filter(ItemModel.id == item_id).first()

def get_all_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ItemModel).offset(skip).limit(limit).all()

def create_new_item(db: Session, item: ItemCreate):
    db_item = ItemModel(name=item.name, price=item.price, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_item_by_id(db: Session, item_id: int):
    db_item = get_item_by_id(db, item_id)
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item