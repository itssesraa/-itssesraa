from typing import Union
Nnumber=[1,2,3,4,5,6,7]
print(Nnumber)
Nnumber[2]=10
print(Nnumber)
data = [10,"Ali",True,3.14]
print(data)

####################################Tube not edit 
Nnumber=(1,2,3,4,5,6,7)
print(Nnumber)
print(Nnumber[2])
###################################setcan not dubb
# عمليات المجموعات
# Union
# دمج مجموعتين.
# Intersection
# العناصر المشتركة.
# Difference
# العناصر الموجودة في الأولى فقط.
numbers = {1,2,2,3,3}
print(numbers)
numbers.add(10)
print(numbers)
############################Key : Value DICTIONARY
DATA={'NAME':'AIL','AGE':20}
print(DATA)
print(DATA['NAME'])
print(DATA['AGE'])
age=20
if age>=18:
    print("You are adult")
else:
    print("You are not adult")  
 
 
a=10
if a>0:
    print("Positive")

if a<0:
    print("Negative")
elif a==0:
    print("Zero")                   
    
fruits = ["Apple", "Banana", "Orange"]

for fruit in fruits:
    print(fruit)    
    
    
###################################
class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def display(self):
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")
        print("-" * 30)

#####################################
def display_products():
    print("Available products:")
    print("-" * 30)
    for product, price in products.items():
        print(f"{product.capitalize()}: {price} EGP")
products = {
    "milk": 40,
    "bread": 10,
    "rice": 20,
    "juice": 30,
    "cheese": 30
}
cart = []
###############
def calc_item_total(item, quantity):
    
    if item in products:
        total_price = products[item] * quantity
        return total_price
    else:
        print(f"{item.capitalize()} is not available.")
        return 0
################################3
def add_to_cart(item, quantity):

    if item in products:
        cart.append((item, quantity))
        print(f"{quantity} {item}(s) added to the cart.")
    else:
        print(f"{item.capitalize()} is not available.")
        
products = {
            "milk": 40,
            "bread": 10,
            "rice": 20,
            "juice": 30,
            "cheese": 30
        }
cart = []


####
def add_to_cart(item, quantity):
    product = {
        "name": item,
        "quantity": quantity
    }
    cart.append(product)
    print(f"Added {quantity}x {item} to cart.")
    
#########################################
def get_discound_reat_total():
    total = sum(products[item] * quantity for item, quantity in cart)
    discount_rate = 0.15  # 15% discount
    discount_amount = total * discount_rate
    discounted_total = total - discount_amount
    return discounted_total
##########################
def get_discount_rate(total):
  if total >= 500:
    return 0.15
  elif total >= 300:
    return 0.10
  elif total >= 200:
    return 0.05
  else:
    return 0.0
################################################

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
while True:
   print(f'''
   Welcome to our program:
   Choose option:
   1. to show all products
   2. add item to card
   3. show price before discount
   4. show price after discount
   5. free cart
   6. Exit
   ''')

   choice = int(input('Enter your choice: '))
   if choice == 1:
      display_products()
   elif choice == 2:
      item = input('Enter item from our product list: ')
      quantity = int(input('Enter quantity: '))
      add_to_cart(item, quantity)
   elif choice == 3:
        total_before = calculate_total_cart_invoice()
        print(f'Total invoice before discount is: {total_before}')
   elif choice == 4:
        total_after = calculate_fianl_price()
        print(f'Total invoice after discount is: {total_after}')
   elif choice == 5:
        free_cart()
        print(f'cart is free now')
   elif choice == 6:
        break
   else:
       print('5aleek mo7taram and choose from give list')
 #################################################################################################
 