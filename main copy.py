from db import models
from db.database import get_db, database_engine
from fastapi import Depends, FastAPI, HTTPException, Response, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from router import auth, order, product, raw_material, user, metals, image
from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=database_engine)


app = FastAPI()
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(product.router)
app.include_router(raw_material.router)
app.include_router(order.router)
app.include_router(image.router)
app.include_router(metals.router)
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


################# declaration of the exception ##################

incorrectException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Incorrect username or password ",
    headers={"WWW-Authenticate": "Bearer"}
)
