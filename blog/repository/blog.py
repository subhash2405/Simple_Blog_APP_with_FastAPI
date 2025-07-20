from fastapi import APIRouter, Depends, status
from fastapi.responses import Response
from blog import models, schemas
from blog.database import get_db
from sqlalchemy.orm import Session
from typing import List

# db = get_db()



def get_all(db : Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create_blog(blog: schemas.BaseBlog, db: Session):
    new_blog = models.Blog(title = blog.title, content = blog.content, owner_id = 1)  # Assuming owner_id is set to 1 for simplicity
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    
    return new_blog

def get_blog(blog_id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not blog:
        return None
    return blog

def delete_blog(blog_id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not blog:
        return None
    db.delete(blog)
    db.commit()
    return blog

def update_blog(id: int, blog: schemas.BaseBlog, db: Session):
    existing_blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not existing_blog:
        return None
    
    existing_blog.title = blog.title
    existing_blog.content = blog.content
    db.commit()
    db.refresh(existing_blog)
    
    return existing_blog