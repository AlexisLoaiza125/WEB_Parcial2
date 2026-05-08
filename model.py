from sqlmodel import Field, SQLModel

from datetime import datetime, timezone


class Dog(SQLModel, table = True):
    id: int
    name: str
    size: str
    dangerous: bool
    sterilized: bool
    breed: str
    img: str
    created: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class DogUpdate(SQLModel):
    name: str = None
    size: str = None
    breed: str = None