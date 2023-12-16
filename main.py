from fastapi import FastAPI, Depends, HTTPException, Security
from sqlalchemy.orm import Session
from fastapi.security import HTTPBearer
from typing import List
# import models  # import your SQLAlchemy models
import schemas  # import your Pydantic schemas

from utils import VerifyToken
from db import SessionLocal, PostDB

app = FastAPI()

token_auth_scheme = HTTPBearer()
auth = VerifyToken()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/api/public")
def public():
    """No access token required to access this route"""

    result = {
        "status": "success",
        "msg": ("Hello from a public endpoint! You don't need to be "
                "authenticated to see this.")
    }
    return result

# Create
@app.post("/api/posts/", response_model=schemas.PostCreate)
async def create_post(post: schemas.PostCreate, db: Session = Depends(get_db), auth_result: str = Security(auth.verify)):
    db_post = PostDB(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

# List
@app.get("/api/posts/", response_model=List[schemas.Post])
async def read_all_posts(db: Session = Depends(get_db)):
    posts = db.query(PostDB).all()
    return posts

# Read
@app.get("/api/posts/{post_id}", response_model=schemas.Post)
async def read_post(post_id: int, db: Session = Depends(get_db)):
    db_post = db.query(PostDB).filter(PostDB.id == post_id).first()
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post

# Update
@app.put("/api/posts/{post_id}", response_model=schemas.Post)
async def update_post(post_id: int, post: schemas.PostUpdate, db: Session = Depends(get_db)):
    db_post = db.query(PostDB).filter(PostDB.id == post_id).first()
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")

    post_data = post.dict(exclude_unset=True)
    for key, value in post_data.items():
        setattr(db_post, key, value)

    db.commit()
    db.refresh(db_post)
    return db_post

# Delete
@app.delete("/api/posts/{post_id}", status_code=204)
async def delete_post(post_id: int, db: Session = Depends(get_db)):
    db_post = db.query(PostDB).filter(PostDB.id == post_id).first()
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")

    db.delete(db_post)
    db.commit()
    return {"message": "Post deleted successfully"}
