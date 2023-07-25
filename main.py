from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def demo():
    return {"message": "Hello World"}