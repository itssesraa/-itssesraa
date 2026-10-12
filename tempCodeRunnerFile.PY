
def calculate_total(cart):
    for item, quantity in cart:
        if item not in products:
            print(f"{item.capitalize()} is not available.")
            return 0
    total = sum(products[item] * quantity for item, quantity in cart)
    return total
products = {
            "milk": 40,
            "bread": 10,
            "rice": 20,
            "juice": 30,
            "cheese": 30
        }
cart = []    