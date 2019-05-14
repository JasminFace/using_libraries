from product import *

class Cart:
    def __init__(self):
        self.items = []
    
    def __str__(self):
        return "\n".join([str(item) for item in self.items])

    def add_item(self,item):
        self.items.append(item)
    
    def remove_item(self,item):
        self.items.remove(item)

    def subtotal(self):
        subtotal = 0
        for item in self.items:
            subtotal += item.price
        return f"Your subtotal is ${subtotal:.2f}"

    def cart_total(self):
        total = 0
        for item in self.items:
            total += item.total_price()
        return f"Your total is ${total:.2f}"

    #nMOVED THIS LINE TO __str__
    # def list_items(self):
    #     return "\n".join([str(item) for item in self.items])

apple = Product("Apple", 1.76)
mango = Product("Mango", 2.43)
eggs = Product("Carton of eggs", 6.52)
rice = Product("Jasmine Rice", 11.41)
avocado = Product("Avocado", 3.66)
popcorn = Product("Box of Popcorn", 4.79)

cart = Cart()

cart.add_item(apple)
cart.add_item(mango)
cart.add_item(eggs)
cart.add_item(rice)
cart.add_item(avocado)
print(cart)
print(cart.subtotal())
print("-------------------")

cart.remove_item(avocado)
print(cart)
print(cart.subtotal())
print("-------------------")

cart.add_item(popcorn)
print(cart)
print(cart.subtotal())
print("-------------------")


print(cart.cart_total())