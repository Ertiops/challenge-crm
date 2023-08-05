from fastapi import APIRouter, WebSocket, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


booking = APIRouter()


booking.mount("/booking", StaticFiles(directory="./static"), name="static")
templates = Jinja2Templates(directory="./templates")


@booking.post("/", response_class=HTMLResponse, tags=["booking"])
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})