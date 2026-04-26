# from NewProduct import Product, PerishableProduct, ElectronicProduct, ClothingProduct


class ProductMenu:

    def __init__(self):
        self.action_choice = self.run_until_valid(self.action_choice_validate_fn)

        print("Action")
        print(self.action_choice)
        self.define_operation()

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

    def run_until_valid(self, fn):
        result = fn()

        if not result:
            return self.run_until_valid(fn)

        return result


    def product_choice_validate_fu(self):
        action_list = ["1", "2", "3", "4"]
        action_choice = input(
            "\n1.General 2.Perishable 3.Electronic 4.Clothing:\n"
        )
        if action_choice in action_list:
            return action_choice
        else:
            print("\nInvalid choice, TRY AGAIN")
            return False



    def define_operation(self):
        if self.action_choice == "1":
            print("action selected 2 add")

            # TASK
            # 1 GET PRODUCT TYPE
            # 2 GET PRODUCT DETAILS
            pass
        elif self.action_choice == "2":
            print("action selected 2 update")
        elif self.action_choice == "3":
            print("action selected 2 Delete")
        elif self.action_choice == "4":
            print("action selected 2 Search")
        elif self.action_choice == "5":
            print("action selected. View All")
        elif self.action_choice == "6":
            print("action selected Low Stock")
        else:
            print("INVALID AGAIN")


pm = ProductMenu()
