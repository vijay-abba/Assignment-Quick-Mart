from pathlib import Path
import json

file_path = Path("data")
file_name = file_path / f"products.txt"


class Product:

    def __init__(self):
        # connect to database / product txt
        self.product_list = ""
        self.read_from_file()

    def read_from_file(self):
        with open(file_name, "r") as f:
            str_product_list = f.readline()
            product_list = json.loads(str_product_list)
            self.product_list = product_list

    def writ_to_file(self):
        str_product_list = json.dumps(self.product_list)
        with open(file_name, "w") as f:
            f.write(str_product_list)
        self.read_from_file()

    def add(self, name, quantity, price):

        id = f"PRD-{len(self.product_list)+1:04d}"
        new_product_obj = {
            "id": id,
            "name": name,
            "quantity": quantity,
            "price": price,
            "type": "1",
        }

        self.product_list.append(new_product_obj)
        self.writ_to_file()

    def update(self, id, name, quantity, price):

        new_product_obj = {
            "id": id,
            "name": name,
            "quantity": quantity,
            "price": price,
            "type": "1",
        }
        self.delete(id)
        self.product_list.append(new_product_obj)
        self.writ_to_file()

    def delete(self, id):

        self.product_list = list(
            filter(lambda item: item["id"] != id, self.product_list)
        )
        self.writ_to_file()

    def search(self, name):
        filtered_list = list(
            filter(
                lambda x: x["name"].lower().startswith(name.lower()), self.product_list
            )
        )
        print(filtered_list)

    def view_all(self):

        for i in self.product_list:
            # print(f'{i["id"]} {i["name"]} {i["quantity"]}')
            print(i)

    def lowstock(self):
        filtered_list = list(filter(lambda x: x["quantity"] < 5, self.product_list))
        print(filtered_list)


class PerishableProduct(Product):
    def __init__(self):
        super().__init__()

    def add(self, name, quantity, price, expiry_date):

        id = f"PRD-{len(self.product_list)+1:04d}"
        new_product_obj = {
            "id": id,
            "name": name,
            "quantity": quantity,
            "price": price,
            "type": "2",
            "expiry_date": expiry_date,
        }

        self.product_list.append(new_product_obj)
        self.writ_to_file()

    def update(self, id, name, quantity, price, expiry_date):

        new_product_obj = {
            "id": id,
            "name": name,
            "quantity": quantity,
            "price": price,
            "type": "2",
            "expiry_date": expiry_date,
        }
        self.delete(id)
        self.product_list.append(new_product_obj)
        self.writ_to_file()


class ElectronicProduct(Product):
    def __init__(self):
        super().__init__()

    def add(self, name, quantity, price, warranty):

        id = f"PRD-{len(self.product_list)+1:04d}"
        new_product_obj = {
            "id": id,
            "name": name,
            "quantity": quantity,
            "price": price,
            "type": "3",
            "warranty": warranty,
        }

        self.product_list.append(new_product_obj)
        self.writ_to_file()

    def update(self, id, name, quantity, price, warranty):

        new_product_obj = {
            "id": id,
            "name": name,
            "quantity": quantity,
            "price": price,
            "type": "3",
            "warranty": warranty,
        }
        self.delete(id)

        self.product_list.append(new_product_obj)
        self.writ_to_file()


class ClothingProduct(Product):
    def __init__(self):
        super().__init__()

    def add(self, name, quantity, price, size, material):
        id = f"PRD-{len(self.product_list)+1:04d}"
        new_product_obj = {
            "id": id,
            "name": name,
            "quantity": quantity,
            "price": price,
            "type": "4",
            size: "size",
            material: "material",
        }

        self.product_list.append(new_product_obj)
        self.writ_to_file()

    def update(self, id, name, quantity, price, size, material):
        new_product_obj = {
            "id": id,
            "name": name,
            "quantity": quantity,
            "price": price,
            "type": "4",
            size: "size",
            material: "material",
        }
        self.delete(id)

        self.product_list.append(new_product_obj)
        self.writ_to_file()


"""
p1 = Product()
p1.add("BOOK1", 25)  # name,  quantity

pp2 = PerishableProduct()
pp2.add("Milk", 30, "10 May 2026")  # expiry_date

ep3 = ElectronicProduct()  #
ep3.add("Samsung s26", 50, "2 Years")  # warranty


cp4 = ClothingProduct()
cp4.add("BluE ShIrt", 20, "M", "Silk")  #  size, material


print("---")
p1.view_all()
print("---")
pp2.view_all()
print("---")
ep3.view_all()
print("---")
cp4.view_all()
print("---")

"""

"""
p1 = Product()

# pp2 = PerishableProduct()

# ep3 = ElectronicProduct()

cp4 = ClothingProduct()

p1.view_all()
print("---")

# check id exists
# cp4.update("PRD-0004","Navy Blue Shirt", 30, "M", "Pure Silk")
cp4.view_all()
print("---")


# p1.delete("PRD-0004")

p1.view_all()
print("---")

p1.search("bo")

p1.add("Pen1", 3)

p1.lowstock()
"""