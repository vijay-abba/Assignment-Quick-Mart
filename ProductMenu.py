
from NewProduct import Product, PerishableProduct, ElectronicProduct, ClothingProduct


class ProductMenu:

    products = []

    def __init__(self):
        print("\n===== Inventory =====")
        action_choice = self.initizial(self.action_choice_validate_fn)
        product_choice = self.initizial(self.product_choice_validate_fn)

        self.define_operstion(action_choice, product_choice)

    def action_choice_validate_fn(self):
        action_list = ["1", "2", "3", "4", "5", "6"]
        action_choice = input(
            "\n1.Add  2.Update  3.Delete 4.Search  5.View All  6.Low Stock:\n"
        )
        if action_choice in action_list:
            return action_choice
        else:
            print("\nInvalid choice, TRY AGAIN")
            return False

    def product_choice_validate_fn(self):
        product_list = ["1", "2", "3", "4"]
        product_choice = input("\n1-General 2-Perishable 3-Electronic 4-Clothing:\n")

        if product_choice in product_list:
            return product_choice
        else:
            print("\nInvalid choice, Please Try Again!")
            return False

    def initizial(self, fn):
        result = fn()

        if not result:
            return self.initizial(fn)

        return result

    def define_operstion(self, action_choice, product_choice):

        if action_choice == "1":
            self.add_product(product_choice)
        elif action_choice == "2":
            self.update_product(product_choice)
        elif action_choice == "3":
            self.delete_product(product_choice)
        elif action_choice == "4":
            self.search_product(product_choice)
        elif action_choice == "5":
            self.view_product(product_choice)
        elif action_choice == "6":
            self.low_stock_product(product_choice)
        else:
            print("INVALID AGAIN")

    def add_product(self, product_choice):
        print("Add product")
        id = f"PRD-{len(self.products)+1:04d}"

        if product_choice == "1":
            name = input("Name: ")
            quantity = input("Quantity: ")
            p1 = Product(id, name, quantity)
            p1.details()
            ProductMenu.products.append(p1)
            print(ProductMenu.products)
        elif product_choice == "2":
            name = input("Name: ")
            quantity = input("Quantity: ")
            expiry_date = input("expiry_date: ")
            p2 = PerishableProduct(id, name, quantity, expiry_date)
            ProductMenu.products.append(p2)
            print(ProductMenu.products)

    def update_product(self, product_choice):
        print("Update product")
        print("product choice", product_choice)

    def delete_product(self, product_choice):
        print("Delete product")
        print("product choice", product_choice)

    def search_product(self, product_choice):
        print("Search product")
        print("product choice", product_choice)

    def view_product(self, product_choice):
        print("View All product")
        print("product choice", product_choice)

    def low_stock_product(self, product_choice):
        print("Low Stock product")
        print("product choice", product_choice)


p1 = ProductMenu()
