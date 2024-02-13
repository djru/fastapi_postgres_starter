from typing import List
from fastapi import APIRouter, HTTPException
from src.orders.models import Order
from src.orders.repo import OrdersRepo

router = APIRouter()


@router.get("/orders")
async def orders(limit: int = 10) -> List[Order]:
    repo = OrdersRepo()
    orders = repo.get_orders(limit)
    return orders


@router.get("/order/{id}")
async def order(id: int) -> Order:
    repo = OrdersRepo()
    order = repo.find_order(id)
    if not order:
        raise HTTPException(status_code=404, detail=f"Order not found. order_id={id}")
    return order
