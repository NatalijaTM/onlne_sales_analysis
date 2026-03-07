from ProductManager import ProductManager
from product import Product

# Kreiranje instance ProductManager
manager = ProductManager()

# Dodavanje nekoliko proizvoda
p1 = Product("Mleko", 120, 30)
p2 = Product("Hleb", 60, 50)
p3 = Product("Jaja", 20, 300)

manager.products.append(p1)
manager.products.append(p2)
manager.products.append(p3)

# Prikaz svih proizvoda
print("Lista proizvoda: ")
manager.display_all_products()

# Prikaz ukupne vrednosti inventara
print("Ukupna vrednost inventara: ")
manager.total_value()
