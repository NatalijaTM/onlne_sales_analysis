from ProductManager import ProductManager
from product import Product
from cart import Cart
import random

# Kreiranje instance ProductManager
manager = ProductManager()

# Dodavanje nekoliko proizvoda
p1 = Product("Mleko", 120, 30)
p2 = Product("Hleb", 60, 50)
p3 = Product("Jaja", 20, 300)
p4 = Product("Sir", 500, 10)
p5 = Product("Brašno", 80, 30)

manager.products.append(p1)
manager.products.append(p2)
manager.products.append(p3)
manager.products.append(p4)
manager.products.append(p5)

# Prikaz svih proizvoda
print("Lista proizvoda: ")
manager.display_all_products()

# Prikaz ukupne vrednosti inventara
print("Ukupna vrednost inventara: ")
manager.total_value()

# Kreiranje instance Cart
my_cart = Cart()

# Dodavanje 3 slučajno odabrana proizvoda u korpu
if len(manager.products) >= 3:
    random_products = random.sample(manager.products, 3)
else:
    random_products = manager.products

for product in random_products:
    quantity = random.randint(1, product.quantity)
    my_cart.add_to_cart(product, quantity)

# Prikaz korpe i ukupne vrednosti
print()
print("Sadržaj korpe i ukupna vrednost:")
print ("------------------------------------------------")
my_cart.display_cart()
