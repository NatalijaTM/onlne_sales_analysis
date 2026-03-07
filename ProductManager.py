from product import Product
class ProductManager:
    def __init__(self):
        self.products = []   #lista svih proizvoda kao atribut

    #Dodavanje proizvoda
    def add_product(self):
        name = input("Unesite naziv proizvoda: ")
        price = float(input("Unesite cenu proizvoda: "))
        quantity = int(input("Unesite količinu proizvoda: "))
        new_product = Product(name, price, quantity)
        self.products.append(new_product)
        print("Proizvod je uspešno dodat.\n")

    #Prikaz svih proizvoda
    def display_all_products(self):
        if not self.products:
            print("Lista proizvoda je prazna.")
            return
        for product in self.products:
            product.display_product_info()

    #Ukupna vrednost svih proizvoda
    def total_value(self):
        total = 0
        for product in self.products:
            total += product.price * product.quantity
        print(f"Ukupna vrednost svih proizvoda je: {total}")
        