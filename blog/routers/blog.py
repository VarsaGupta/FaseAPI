from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from blog import schemas, database, models

router = APIRouter(
     tags=['blog']
)


@router.get("/blog")
def get_blog(db : Session = Depends(database.get_db)):
    blogs = db.query(models.Blog).all()
    return blogs 