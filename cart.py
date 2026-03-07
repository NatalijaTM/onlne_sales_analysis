from product import Product

class Cart:
    def __init__(self):
        self.cart_items = []  # Lista proizvoda u korpi

    # Dodavanje proizvoda u korpu
    def add_to_cart(self, product, quantity):
        if quantity > product.quantity:
            print(f"Nema dovoljno proizvoda na stanju. Dostupno je: {product.quantity}")
            return
        self.cart_items.append((product, quantity))
        print(f"Dodato {quantity} x {product.name} u korpu.")

    # Računanje ukupne vrednosti korpe
    def total_amount(self):
        total = 0
        for product, quantity in self.cart_items:
            total += product.price * quantity
        return total

    # Prikaz sadržaja korpe
    def display_cart(self):
        if not self.cart_items:
            print("Korpa je prazna.")
            return

        print("Sadržaj korpe: ")
        for product, quantity in self.cart_items:
            print (f"{product.name} - {quantity} x {product.price} = {product.price * quantity}")
            print ("-----------------------------------------------")
        print(f"Ukupno za naplatu: {self.total_amount()}")
        