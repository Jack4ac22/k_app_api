from fastapi import FastAPI
from db import models
from db.database import database_engine
from routers import user, person, image, phone, auth, comment, task, job_title, person_job_title

app = FastAPI()
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(person.router)
app.include_router(job_title.router)
app.include_router(person_job_title.router)
app.include_router(phone.router)
app.include_router(comment.router)
app.include_router(task.router)
app.include_router(image.router)


models.Base.metadata.create_all(bind=database_engine)
