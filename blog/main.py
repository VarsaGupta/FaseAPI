from fastapi import FastAPI, Depends, status, Response, HTTPException
from blog import schemas, models
from blog.database import engine, get_db
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from blog.routers import blog,user

app = FastAPI()

models.Base.metadata.create_all(engine)

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()    

app.include_router(blog.router)
app.include_router(user.router)


@app.post("/blog", status_code= status.HTTP_201_CREATED, tags=['blog'])
def createBlog(request : schemas.Blog, db : Session = Depends(get_db)):
    new_blog = models.Blog(title = request.title, body = request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

# @app.get("/blog", tags=['blog'])
# def get_blog(db : Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs 

@app.get("/blog/{id}", status_code=200, tags=['blog'])
def showBlog(id, response: Response, db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f'Blog with the id {id} is not available')
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f'Blog with the id {id} is not available'}
    return blog

@app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED,tags=['blog'])
def update(id, request : schemas.Blog, db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"blog with id {id} does not exist")
    blog.update(request.dict())
    db.commit()
    return {f'Successfully Updated the blog with id {id}'}


@app.delete("/blog/{id}", status_code= status.HTTP_204_NO_CONTENT, tags=['blog'])
def destroy(id, db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"blog with id {id} does not exist")
    blog.delete(synchronize_session = False)
    db.commit()
    return {'message':'The blog with id {id} is deleted'}


# pwd_cxt = CryptContext(schemes=["bcrypt"],  deprecated="auto")

# @app.post('/user', tags=['blog'])
# def create_user(request: schemas.User, db : Session = Depends(get_db)):

#     hashedPassword = pwd_cxt.hash(request.password)
#     new_user = models.User(name=request.name, email= request.email, password = hashedPassword)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

