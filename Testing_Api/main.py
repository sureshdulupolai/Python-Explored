# main.py

from dummy_api import ProductAPI, OrderAPI

# Initialize APIs
product_api = ProductAPI()
order_api = OrderAPI(product_api.get_all_products())

# Get all products
print("Products:", product_api.get_all_products())

# Get a product by ID
print("Product ID 2:", product_api.get_product_by_id(2))

# Generate 3 dummy orders
dummy_orders = order_api.get_all_orders(3)
for order in dummy_orders:
    print(order)
