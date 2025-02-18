from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str


@app.get("/")
async def root():
    return {"message": "Welcome to my api."}


@app.get("/posts")
def get_posts():
    return {"data": "This is your posts."}


# @app.post("/createposts")
# def create_posts(payload: dict = Body(...)):
#     print(payload)
#     return {"new_post": f"title {payload['title']} content: {payload['content']}"}

# title str, content str (specifying using pydantic)
@app.post("/createposts")
def create_posts(new_post: Post):
    print(new_post)
    print(new_post.title)
    return {"data": "new-post"}
