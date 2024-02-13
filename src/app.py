from fastapi import FastAPI

from src.orders.routes import router as orders_router

app = FastAPI()


@app.get("/")
async def root() -> str:
    return "hello you"


# attach routers
app.include_router(orders_router)
