from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from service import trello, get_list


app = FastAPI(title='Space-X Api', description='API - Trello')

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Card(BaseModel):
    list: str
    name: str
    desc: str

@app.get("/")
async def test():
    return "I'm ready!"

@app.get("/list")
async def list():

    response = get_list()
    return response

@app.post("/cards")
async def create_card(request: Card, status_code=201):
    event = {
        'list': request.list,
        'name': request.name,
        'desc': request.desc,
    }

    response = trello(event)
    return response