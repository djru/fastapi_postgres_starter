from datetime import date
from unittest import TestCase
from unittest.mock import MagicMock, patch
from fastapi import FastAPI
from src.orders.routes import router
from fastapi.testclient import TestClient
from src.orders.models import Order


class OrdersRouteTest(TestCase):
    def setUp(self) -> None:
        # patch repo
        self.repo_patcher = patch("src.orders.repo.OrdersRepo.__new__")
        self.repo_mocker = self.repo_patcher.start()
        self.repo = MagicMock()
        self.repo_mocker.return_value = self.repo

        # setup api
        api = FastAPI()
        api.include_router(router)
        self.client = TestClient(api)
        return super().setUp()

    def tearDown(self) -> None:
        self.repo_patcher.stop()
        return super().tearDown()

    def test_happy(self):
        self.repo.get_orders.return_value = [
            Order(
                order_id=1,
                ship_name="Dan",
                ship_city="Chicago",
                order_date=date.today(),
            ),
            Order(
                order_id=2,
                ship_name="Fred",
                ship_city="Milwaukee",
                order_date=date.today(),
            ),
        ]
        resp = self.client.get("/orders")
        print(resp.json())
        self.assertEqual(
            resp.json(),
            [
                {
                    "order_id": 1,
                    "name": "Dan",
                    "city": "Chicago",
                    "date": "2024-02-12",
                },
                {
                    "order_id": 2,
                    "name": "Fred",
                    "city": "Milwaukee",
                    "date": "2024-02-12",
                },
            ],
        )

    def test_bogus_param(self):
        self.repo.get_orders.return_value = [
            Order(
                order_id=1,
                ship_name="Dan",
                ship_city="Chicago",
                order_date=date.today(),
            )
        ]
        resp = self.client.get("/orders?limit=blue")
        self.assertEqual(resp.status_code, 422)
