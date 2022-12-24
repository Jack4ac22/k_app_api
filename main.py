from fastapi import FastAPI
from db import models
from db.database import database_engine

app = FastAPI()


@app.get('/')
def test():
    return "the server is running."


models.Base.metadata.create_all(bind=database_engine)
