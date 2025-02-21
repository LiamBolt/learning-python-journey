from fastapi import FastAPI, Depends, status, HTTPException, Response
from . import models, schemas, utils
from .database import engine, get_db
from sqlalchemy.orm import Session
from typing import List
from .routers import post, user



models.Base.metadata.create_all(bind=engine)

app = FastAPI()



app.include_router(post.router)
app.include_router(user.router)

