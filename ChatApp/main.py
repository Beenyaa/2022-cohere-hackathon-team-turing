import json
from fastapi import (
    FastAPI, WebSocket, WebSocketDisconnect, Request, Response
)
from typing import List
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()

app.mount(
    "/static", StaticFiles(directory=str(Path(BASE_DIR, 'static'))), name='static')

# locate templates
templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))


@app.get("/")
def get_home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/customer-chat")
def get_customerChat(request: Request):
    return templates.TemplateResponse("customerChat.html", {"request": request})


@app.get("/customer-support")
def get_customerSupportChat(request: Request):
    return templates.TemplateResponse("customerSupportChat.html", {"request": request})


class RegisterValidator(BaseModel):
    username: str

    class Config:
        orm_mode = True


class SocketManager:
    def __init__(self):
        self.active_connections: List[(WebSocket, str)] = []

    async def connect(self, websocket: WebSocket, user: str):
        await websocket.accept()
        self.active_connections.append((websocket, user))

    def disconnect(self, websocket: WebSocket, user: str):
        self.active_connections.remove((websocket, user))

    async def broadcast(self, data: dict):
        for connection in self.active_connections:
            await connection[0].send_json(data)


manager = SocketManager()


def postMessage(msg):
    ...


templates.env.globals.update(postMessage=postMessage)


async def handleCustomerSupport(data):
    print(data)
    await manager.broadcast(data)


async def handleCustomer(data):
    values = ['hellow', 'abc', 'korea']
    msg = {'type': 'multichoice', 'sender': 'Customer Support', 'messages': values}
    
    print(msg)
    await manager.broadcast(msg)


async def handleCustomerSupportBot(data):
    await manager.broadcast(data)


@app.websocket("/api/chat/{sender}")
async def chat(websocket: WebSocket, sender):
    if sender:
        await manager.connect(websocket, sender)
        response = {
            "sender": sender,
            "message": "got connected"
        }
        try:
            await manager.broadcast(response)
            while True:
                data = await websocket.receive_json()

                match sender:
                    case "Customer Support":
                        await handleCustomerSupport(data)

                    case "Customer":
                        await handleCustomer(data)

                    case "Customer Support Bot":
                        await handleCustomerSupportBot(data)

        except WebSocketDisconnect:
            manager.disconnect(websocket, sender)
            response['message'] = "left"
            await manager.broadcast(response)
