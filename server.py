from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


app = FastAPI()

users = [
    (1,'tiago','senha1'),
    (2,'marta','senha2'),
]

@app.get('/')
def home():
    return {'message': 'World Again!'}

@app.get('/cadastro')
def cadastro():
    return {'message': 'Cadastro'}

@app.get('/login')
def login():
    return {'message': 'Login'}

 
@app.get('/test/{id}')
def test(id: int):
    result = None
    for cada in users:
        if cada[0] == id:
           result = cada
    if not result: return {'message': 'not found'}
    obj = {}
    obj['id']=result[0]
    obj['name']=result[1]
    obj['pass']=result[2]
    return {'message': obj}


class User(BaseModel):
    id: int
    name: Optional[str]
    pasw: str

lista = [
    User(id=1,name='tiago',pasw='123'),
    User(id=2,name='marta',pasw='124'),
    User(id=3,name='catarina',pasw='125'),
    User(id=3,name='beatriz',pasw='126'),
]

@app.post('/users')
def user(user: User):
    lista.append(user)
    return user



@app.get('/users')
def user():
    return lista



