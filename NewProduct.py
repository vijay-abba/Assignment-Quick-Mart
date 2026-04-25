from pathlib import Path
import json

file_path = Path("data")
file_name = file_path / f"products.txt"


class Product:

    def __init__(self):
        # connect to database / product txt
        self.product_list = self.read_from_file()


    def read_from_file(self):
        with open(file_name, "r") as f:
            str_product_list = f.readline()
            product_list = json.loads(str_product_list)
            return product_list

    def writ_to_file(self):
        str_product_list = json.dumps(self.product_list)
        with open(file_name, "w") as f:
            f.write(str_product_list)

    def add(self, name, quantity):
        id = f"PRD-{len(self.product_list)+1:04d}"
        new_product_obj = {"id": id, "name": name, "quantity": quantity}

        self.product_list.append(new_product_obj)
        self.writ_to_file()

    def update(self, id, name, quantity):
        new_product_obj = {"id": id, "name": name, "quantity": quantity}
        self.delete(id)
        self.product_list.append(new_product_obj)
        self.writ_to_file()

    def delete(self, id):
        self.product_list = list(
            filter(lambda item: item["id"] != id, self.product_list)
        )
        self.writ_to_file()

    def search(self, name):
        filtered_list = list(filter(lambda x: x["name"].lower().startswith(name.lower()), self.product_list))
        print(filtered_list)

    def view_all(self):
        for i in self.product_list:
            print(f'{i["id"]} {i["name"]} {i["quantity"]}')

    def lowstock(self):
        filtered_list = list(filter(lambda x : x["quantity"] < 5, self.product_list))
        print(filtered_list)


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


p1 = Product()

# p1.add("vijay", 25)
# p1.delete("PRD-0004")

# p1.update("PRD-0001", "books", 3)
# p1.view_all()

# p1.search("vIJ")
p1.lowstock()
