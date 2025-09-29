from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return{"message:welcome to TODO API"}

@app.get("/hello")
def say_hello():
        return {"message": "Hello merged version!"}


#wassup noon
todos = []

@app.get("/todos")
def get_todos():
    return todos

@app.get("/todos")
def add_todo(item:str)
    todos.append(item)
    return{"status":"added", "item":item}
