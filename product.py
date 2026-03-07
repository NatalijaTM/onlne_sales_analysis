class Product: #Klasa proizvoda
    #Konstruktor za unos podataka
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)
        
    #Metoda za štampanje podataka
    def display_product_info(self):
        print(f"Naziv proizvoda: {self.name}")
        print(f"Cena proizvoda: {self.price}")
        print(f"Količina proizvoda dostupna na stanju: {self.quantity}")
        print("--------------------------------------------------")
    
    #Metoda za promenu količine proizvoda
    def change_product_quantity(products):
        ime_proizvoda = input("Uneti naziv proizvoda kome se menja količina: ")
        pronadjen = False
        for item in products:
            if ime_proizvoda == item.name:
                new_quantity = int(input("Uneti novu količinu: "))
                item.quantity = new_quantity
                pronadjen = True
                print("Količina je uspešno promenjena.")
        if not pronadjen:
            print("Traženi proizvod nije pronađen.")
 