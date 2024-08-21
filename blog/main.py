from fastapi import Depends, FastAPI
from . import schemas
from . import models
from .database import engine
from sqlalchemy.orm import Session

app = FastAPI()


models.Base.metadata.create_all(engine)


def get_db():
    db = "" # TODO



@app.post("/blog")
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    return db


