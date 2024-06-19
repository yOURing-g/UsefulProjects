import time

"" """""
Overview
The Grocery List Manager project is a simple program written in Python that helps users manage their grocery list. This project includes functionality to add, remove, update, and view items in the list, as well as to clear the entire list. The program uses a dictionary to store the items and their respective quantities.

Components

1. Dictionary for Storage
   - The `grocery_list` dictionary is used to store items as keys and their quantities as values. This allows for efficient lookups, additions, and deletions.

2. Functions
   - The project is composed of several functions that perform different operations on the grocery list.

Functions

1. add_item(item, quantity)
   - Adds an item to the grocery list or updates the quantity if the item already exists.
   - Parameters:
     - `item` (str): The name of the grocery item.
     - `quantity` (int): The quantity of the item to add.
   - Operation:
     - If the item is already in the list, its quantity is increased by the specified amount.
     - If the item is not in the list, it is added with the specified quantity.

2. remove_item(item, quantity)
   - Removes a specified quantity of an item from the grocery list or deletes the item if the remaining quantity is less than or equal to zero.
   - Parameters:
     - `item` (str): The name of the grocery item.
     - `quantity` (int): The quantity of the item to remove.
   - Operation:
     - If the item is in the list and the quantity to remove is greater than or equal to the current quantity, the item is deleted from the list.
     - If the item is in the list and the quantity to remove is less than the current quantity, the quantity is reduced by the specified amount.

3. update_quantity(item, quantity)
   - Updates the quantity of a specified item in the grocery list.
   - Parameters:
     - `item` (str): The name of the grocery item.
     - `quantity` (int): The new quantity of the item.
   - **Operation:**
     - If the item is in the list, its quantity is set to the specified amount.

4. clear_list()
   - Clears all items from the grocery list.
   - Operation:
     - The `grocery_list` dictionary is cleared, removing all items.

5. view_list()
   - Prints the current items and their quantities in the grocery list.
   - **Operation:**
     - Iterates over the `grocery_list` dictionary and prints each item and its quantity.

"""

shop_info = [
    {"item":"shoe","quantity":16,"price":99.99},
    {"item":"chips","quantity":3,"price":1.99},
    {"item":"chair","quantity":0,"price":99.99}
]
problemOccured=0
cart=[]
money=120
def addToCart(name,quantity,price):
    for item in shop_info:
        if item["item"] == name:
            if item["quantity"] >= quantity:
                item["quantity"] -= quantity
                Information = {
                    "name": name,
                    "quantity": quantity,
                    "price": item["price"]


                }
                cart.append(Information)
                return {
                    "status": True,
                    "message": "Order Successful"
                }

            else:


                return {
                    "status":False,
                    "message":"We dont have enough of this item available"
                }

    return {
        "status": False,
        "message": "We dont have this item"
    }
def Clear():
    cart.clear()
    print("deleted!")

def View():
    print(cart)
    print("This is whats in your cart right now")

def removeItem(name,quantity):
    for item in cart:
        if item["name"] == name:
            if item["quantity"] >= quantity:
                item["quantity"] -= quantity


                return {
                    "status": True,
                    "message": "Deletion Successful"
                }

            else:

                return {
                    "status": False,
                    "message": "You dont have enough of this item "
                }

    return {
        "status": False,
        "message": "You dont have this item"
    }
print("Welcome to the Shop!")
while True:

    time.sleep(1)
    print("What can I do for ya?")
    print("1 to add an item")
    print("2 to remove an item")
    print("3 to view your cart")
    print("4 to clear your whole cart")
    print("5 to Exit the shop")
    print(shop_info)
    try:
        function = int(input(""))
    except:
        print("that input was invalid, please try again")
        print("====================================")

    else:
        print("Uh ok")
        time.sleep(0.5)
        if(function == 1):
            try:
                result = addToCart(input("What do you want to order?"),int(input("How much do you want to order")),0)
            except:
                print("You must have made a mistake doing something, Please try again")
            else:
                if result["status"] == True:
                    print(result["message"])
                    print("Here's whats in your cart right now")
                    print(cart)
                    print("====================================")
                else:
                    print(result["message"])
                    print("====================================")
        elif(function == 2):
            try:
                result = removeItem(input("What do you want to delete?"), int(input("How much do you want to delete")))
            except:
                print("You must have made a mistake doing something, Please try again")
            else:
                if result["status"] == True:
                    print(result["message"])
                    print("Here's whats in your cart right now")
                    print(cart)
                    print("====================================")
                else:
                    print(result["message"])
                    print("====================================")
        elif(function==3):
            print(cart)
        elif(function==4):
            Clear()
        elif(function==5):
            print("Exiting the Shop...")
            time.sleep(1)
            exit(0)









