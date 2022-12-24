from fastapi import FastAPI
from db import models
from db.database import database_engine
from routers import user, person, image

app = FastAPI()
app.include_router(user.router)
app.include_router(person.router)
app.include_router(image.router)


@app.get('/')
def test():
    return "the server is running."


models.Base.metadata.create_all(bind=database_engine)
