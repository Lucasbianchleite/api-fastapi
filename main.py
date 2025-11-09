from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "mudança do main.py"}



