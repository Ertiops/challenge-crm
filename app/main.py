from fastapi import FastAPI

from routers import booking

app = FastAPI()

app.include_router(booking.booking)




# @app.get("/items/{id}", response_class=HTMLResponse)
# async def read_item(request: Request, id: str):
#     return templates.TemplateResponse("item.html", {"request": request, "id": id})