import logging
from typing import List, Optional
from src.db import DBConnectionFactory
from src.orders.models import Order
from psycopg.rows import class_row


class OrdersRepo:
    def __init__(self):
        self.connection = DBConnectionFactory.get_conn()

    def get_orders(self, limit: int = 10) -> List[Order]:
        try:
            with self.connection.cursor(row_factory=class_row(Order)) as cur:
                results = cur.execute(
                    "select order_id, ship_city, order_date, ship_name "
                    "from orders limit %s;",
                    (limit,),
                )
                return results.fetchall()
        except Exception as e:
            logging.error(f"Could not fetch orders. {e}")
            return []

    def find_order(self, id: int) -> Optional[Order]:
        try:
            with self.connection.cursor(row_factory=class_row(Order)) as cur:
                results = cur.execute(
                    "select order_id, ship_city, order_date, ship_name "
                    "from orders where order_id=%s limit 1;",
                    (id,),
                )
                return results.fetchone()
        except Exception as e:
            logging.error(f"Could not fetch orders. {e}")
            return None
