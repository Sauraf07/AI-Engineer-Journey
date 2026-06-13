# Task 2: Shopping Cart System (Easy-Medium)
'''Create an empty cart
Add products
Remove products
Show all products
Show total number of products'''
cart = []
def add_product(product):
    cart.append(product)    
def remove_product(product):
    if product in cart:
        cart.remove(product)
    else:
        print(f"{product} not found in cart.")
def show_products():
    print("Products in Cart:", cart)
def total_products():
    print("Total Number of Products:", len(cart))
# Example usage
add_product("Laptop")
add_product("Smartphone")
add_product("Headphones")
show_products()
total_products()
remove_product("Smartphone")
show_products()
total_products()
