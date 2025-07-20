from fastapi import APIRouter
from blog import schemas, models
from blog.database import get_db
from sqlalchemy.orm import Session
from typing import List
from fastapi import Depends, HTTPException, status
from fastapi.responses import Response
from blog.repository import blog as blog_repo
from blog.oauth2 import get_current_user

router = APIRouter(
    prefix="/blog",
    tags=["Blogs"]
)


@router.get("/",  response_model=List[schemas.ShowBlog], status_code=status.HTTP_200_OK)
async def get_blogs(
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user)
):
    return blog_repo.get_all(db)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_blog(blog: schemas.BaseBlog, db : Session = Depends(get_db),current_user: schemas.User = Depends(get_current_user)):
    return blog_repo.create_blog(blog, db)
    


@router.get("/{blog_id}", response_model=schemas.ShowBlog, status_code=status.HTTP_200_OK)
async def get_blog(blog_id: int,response : Response, db: Session = Depends(get_db), status_code=status.HTTP_200_OK, current_user: schemas.User = Depends(get_current_user)):
    blog = blog_repo.get_blog(blog_id, db)
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Blog not found"
        )
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"error": "Blog not found"}
    return blog

@router.delete("/{blog_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(blog_id : int, db : Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    blog = blog_repo.delete_blog(blog_id, db)
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Blog not found"
        )
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", status_code=status.HTTP_200_OK)
async def update_blog(id : int, blog : schemas.BaseBlog, db : Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user) ):
    existing_blog = blog_repo.update_blog(id, blog, db)
    if not existing_blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Blog not found"
        )
    
    return existing_blog

