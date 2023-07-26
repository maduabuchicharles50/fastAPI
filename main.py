from fastapi import FastAPI

app = FastAPI()


# home
@app.get("/")
def demo():
    return {"message": "blog list"}

#
@app.get("/blog/unpublished")
def unpublished():
    return {"data": 'all unpublished blogs'}

@app.get("/blog/{id}")
def show(id:int):
    return {"data": id}

@app.get("/blog/{id}/comments")
def comments(id):
    return {"data": {'1', '2'}}


