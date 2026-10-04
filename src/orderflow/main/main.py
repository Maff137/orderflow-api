from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def home():
    return {"message": "hello world"} 


@app.get("/api/posts")
def get_posts():
    return posts

