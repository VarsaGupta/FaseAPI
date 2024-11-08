from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from blog import schemas, database, models
from passlib.context import CryptContext


router = APIRouter(
    tags=['user']
)

pwd_cxt = CryptContext(schemes=["bcrypt"],  deprecated="auto")

@router.post('/user')
def create_user(request: schemas.User, db : Session = Depends(database.get_db)):

    hashedPassword = pwd_cxt.hash(request.password)
    new_user = models.User(name=request.name, email= request.email, password = hashedPassword)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user