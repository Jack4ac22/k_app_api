from db import models
from db.database import get_db, database_engine
from fastapi import Depends, FastAPI, HTTPException, Response, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from routers import user, person, image
from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=database_engine)


app = FastAPI()
app.include_router(user.router)
app.include_router(person.router)
# app.include_router(image.router)
app.mount('/images', StaticFiles(directory='images'), name='images')

################# CORS resolving ##################
origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=['*']
)
