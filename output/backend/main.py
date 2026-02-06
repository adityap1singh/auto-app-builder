
from fastapi import FastAPI


app = FastAPI(title="Generated App")


@app.get("/")
def read_root():
    return {"message": "App generated from prompt: Build a blog application"}
