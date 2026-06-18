'''Task 4: Product Price Filter using Lambda + Filter
Objective

Display products whose price is greater than ₹500.'''
products = [
    {"name": "Laptop", "price": 60000},
    {"name": "Mouse", "price": 500},
    {"name": "Keyboard", "price": 1000},
    {"name": "Monitor", "price": 800}
]

filtered_products = list(filter(lambda x: x["price"] > 500, products))
for product in filtered_products:
    print(f"{product['name']}: ₹{product['price']}")