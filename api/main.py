# api/index.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "This is a simple Python Web Page and the file name is main.py"}
