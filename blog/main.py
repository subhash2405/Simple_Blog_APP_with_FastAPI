from fastapi import FastAPI
from blog import models
from blog.database import engine
from blog.routers import blog
from blog.routers import user
from blog.routers import authentication
app = FastAPI()


models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)

