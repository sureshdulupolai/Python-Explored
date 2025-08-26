# dummy_api.py

import random
from datetime import datetime, timedelta

class ProductAPI:
    def __init__(self):
        # Dummy products
        self.products = [
            {"id": 1, "name": "Car Wax", "price": 499.0, "stock": 20},
            {"id": 2, "name": "Vacuum Cleaner", "price": 1299.0, "stock": 15},
            {"id": 3, "name": "Polish Kit", "price": 899.0, "stock": 30},
        ]

    def get_all_products(self):
        return self.products

    def get_product_by_id(self, product_id):
        for p in self.products:
            if p["id"] == product_id:
                return p
        return {"error": "Product not found"}

    def get_random_product(self):
        return random.choice(self.products)

# dummy_api.py continuation

class OrderAPI:
    def __init__(self, products):
        self.products = products

    def generate_dummy_order(self, order_id=1):
        product = random.choice(self.products)
        qty = random.randint(1, 5)
        subtotal = product["price"] * qty
        gst = round(subtotal * 0.18, 2)
        total = round(subtotal + gst, 2)
        delivery_date = datetime.now() + timedelta(days=random.randint(1,5))
        return {
            "order_id": order_id,
            "product": product,
            "quantity": qty,
            "subtotal": subtotal,
            "gst": gst,
            "total": total,
            "delivery_status": random.choice(["pending", "done", "cancel"]),
            "delivery_date": delivery_date.strftime("%Y-%m-%d %H:%M:%S"),
        }

    def get_all_orders(self, count=5):
        return [self.generate_dummy_order(i+1) for i in range(count)]
