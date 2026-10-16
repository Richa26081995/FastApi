from fastapi import FastAPI,Body

app = FastAPI()
TODOS =[
{
    "title": "Learn FastAPI",
    "description": "Learn FastAPI to build APIs",
    "completed": False
},
{
    "title": "Build a project",
    "description": "Build a project using FastAPI",
    "completed": True
},
{
    "title": "Complete the tutorial",
    "description": "Complete the FastAPI tutorial",
    "completed": False
}
]
@app.get("/")
def greet():
    return {"message": "Hello, World!"}


@app.get("/todos/all")
def get_all_todos():
    return TODOS

@app.post("/create/todos")
def create_todo(new_todo=Body()):
    TODOS.append(new_todo)
    return new_todo 

@app.put("/update/todos/")
def update_todo(existing_todo= Body()):
    TODOS[0]=existing_todo
    return existing_todo

@app.delete("/delete/todos/{title}")    
def delete_tod(title):
    for todo_index in range (len(TODOS)):
        if TODOS[todo_index]["title"].lower() == title.lower():
            del TODOS[todo_index]
            return {"message": "Todo deleted successfully"}

@app.get("/todos/completed")  
def get_completed_todos(completed:bool):
    res=[]      
    for todo in TODOS:
        if todo["completed"] == completed:
            res.append(todo)
    return res