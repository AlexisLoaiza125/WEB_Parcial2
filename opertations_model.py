from sqlmodel import Session, select
from model.Dog import Dog
from fastapi import HTTPException, status

def create_dog(session: Session, dog_data: DogCreate, img_path: str = None) -> Dog:
    db_dog = Dog.model_validate(dog_data)


def get_dogs(session: Session, skip: int = 0, limit: int = 10):
    statement = select(Dog).offset(skip).limit(limit)
    return session.exec(statement).all()

def get_dog_by_id(session: Session, dog_id: int):
    dog = session.get(Dog, dog_id)
    # Si no existe O está desactivada, lanzamos 404
    if not dog or not dog.is_active:
        raise HTTPException(status_code=404, detail="Dog not found or inactive")
    return dog

def get_dog_by_name(session: Session, dog_name: str):
    statement = select(Dog).where(Dog.name == dog_name)
    dog = session.exec(statement).first()
    if not dog or not dog.is_active:
        raise HTTPException(status_code=404, detail="Dog not found or inactive")
    return dog

def delete_dog(session: Session, dog_id: int):
    # Buscamos el perro (usamos session.get para incluir los inactivos si quisieras restaurarlos)
    db_dog = session.get(Dog, dog_id)
    if not db_dog:
        raise HTTPException(status_code=404, detail="Dog not found")
    