from fastapi import FastAPI 
app = FastAPI()

@app.get("/welcome")
def Welcome():
    return {"message": "Welcome to mini-RAG!"}
