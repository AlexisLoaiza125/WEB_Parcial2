from typing import List
from fastapi import FastAPI
from db import  SessionDep, create_all_tables
from sqlmodel import select

app = FastAPI()

@app.post("/dog/", response_model=DogPublic)
async def create_dog(
    session: SessionDep,
    id: Annotated[int, Form()],
    name: Annotated[str, Form()],
    size: Annotated[str, Form()],
    dangerous: Annotated[bool, Form()],
    sterilized: Annotated[bool, Form()],
    breed: Annotated[str, Form()],
    img: Annotated[str, Form()] = None
):
    dog_in = DogCreate(id=id, name=name, size=size, dangerous=dangerous, sterilized=sterilized, breed=breed, img=img)
    return dog_ops.create_dog(session, dog_in, img)


@app.get("/dogs/", response_model=List[DogPublic])
def read_dogs(session: SessionDep, skip: int = 0, limit: int = 10):
    return dog_ops.get_dogs(session, skip, limit)

@app.get("/dogs/{dog_id}", response_model=DogPublic)
def read_dog(session: SessionDep, dog_id: int):
    return dog_ops.get_dog_by_id(session, dog_id)

@app.get("/dogs/{dog_name}", response_model=DogPublic)
def read_dog_by_name(session: SessionDep, dog_name: str):
    return dog_ops.get_dog_by_name(session, dog_name)

@app.patch("/dog/{dog_id}", response_model=DogPublic)
def update_dog(session: SessionDep, dog_id: int, dog_data: DogUpdate):
    return dog_ops.update_dog(session, dog_id, dog_data)


@app.delete("/dog/{dog_id}")
def delete_dog(session: SessionDep, dog_id: int):
    return dog_ops.delete_dog(session, dog_id)




@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
