import os
from fastapi import FastAPI, Response, status, HTTPException
# from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from dotenv import load_dotenv
from psycopg2.extras import RealDictCursor
import time

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True

while True:
    
    try:
        # Retrieve environment variables
        db_host = os.getenv("DB_HOST")
        db_name = os.getenv("DB_NAME")
        db_user = os.getenv("DB_USER")
        db_password = os.getenv("DB_PASSWORD")

        # Establish database connection
        conn = psycopg2.connect(
            host=db_host,
            database=db_name,
            user=db_user,
            password=db_password,
            cursor_factory=RealDictCursor
        )
        cursor = conn.cursor()
        print("Database connection was successful!")
        break
    except Exception as error:
        print("Connection to database failed.")
        print("Error:", error)
        time.sleep(2)

cursor.execute(""" SELECT * FROM posts """)
my_posts = cursor.fetchall()
print(my_posts)


def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p
 

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i


@app.get("/")
async def root():
    return {"message": "Welcome to my fast api."}


@app.get("/posts")
def get_posts():
    cursor.execute(""" SELECT * FROM posts """)
    posts = cursor.fetchall()
    print(posts)
    
    if posts == []:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="data is empty")
    return {"data": posts}


# @app.post("/createposts")
# def create_posts(payload: dict = Body(...)):
#     print(payload)
#     return {"new_post": f"title {payload['title']} content: {payload['content']}"}

# title str, content str (specifying using pydantic)
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    cursor.execute(""" 
                   INSERT INTO posts (title, content, published) 
                   VALUES (%s, %s, %s) 
                   RETURNING *
                   """,(post.title, post.content, post.published))
    new_post = cursor.fetchone()
    conn.commit()
    # print(new_post.model_dump())  # dict() is deprecated
    
    return {"data": new_post}


# the {id} represents a path parameter
@app.get("/post/{id}")
def get_post(id: int, response: Response):

   
    cursor.execute(""" SELECT * FROM posts WHERE id = %s """, (id,))
    post = cursor.fetchone()
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"post with id: {id} was not found"}
    return {"post_details": post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    cursor.execute(""" DELETE FROM posts WHERE id = %s returning * """, (id,))
    deleted_post = cursor.fetchone()
    conn.commit()

    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    
    cursor.execute(""" UPDATE posts SET title = %s , content = %s, published = %s WHERE id = %s RETURNING * """, (post.title, post.content, post.published, (id,)))
    
    updated_post = cursor.fetchone()
    conn.commit()

    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    
    return {"data": updated_post}
