from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello World!"}

@app.get("/hello/{name}")
def say_hello_name(name: str):
    return {"message": f"Hello, {name}!"}

@app.get("/user")
def say_user(name: str):
    return {"message": f"{name} user!"}

@app.get("/username/{username}")
def say_hello_user(username: str):
    return {"message": f"{username} user!"}

@app.get("/{name}")
def say_hello(name: str):
    return {"message": f"Hello {name}!"}