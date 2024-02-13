import datetime
from pydantic import BaseModel, Field


class Order(BaseModel):
    order_id: int
    name: str = Field(validation_alias="ship_name")
    city: str = Field(validation_alias="ship_city")
    date: datetime.date = Field(validation_alias="order_date")
