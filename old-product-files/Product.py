class Product:

    def __init__(self, id, name, quantity):
        self.id = id
        self.name = name
        self.quantity = quantity

    def details(self):
        print(self.id)
        print(self.name)
        print(self.name)


class PerishableProduct(Product):
    def __init__(self, id, name, quantity, expiry_date):
        super().__init__(id, name, quantity)
        self.expiry_date = expiry_date


class ElectronicProduct(Product):
    def __init__(self, id, name, quantity, warranty):
        super().__init__(id, name, quantity)
        self.warranty = warranty


class ClothingProduct(Product):
    def __init__(self, id, name, quantity, size, material):
        super().__init__(id, name, quantity)
        self.size = size
        self.material = material

# --- 



class ProductForm:

    def __init__(self, id, name, quantity):
        self.id = id
        self.name = name
        self.quantity = quantity
    
    add 