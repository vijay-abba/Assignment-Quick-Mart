# from NewProduct import Product, PerishableProduct, ElectronicProduct, ClothingProduct


class ProductMenu:

    def __init__(self):
        action_indexs = ["1", "2", "3", "4", "5", "6"]
        action_message = (
            "\n1.Add  2.Update  3.Delete 4.Search  5.View All  6.Low Stock:\n"
        )

        self.action_choice = self.run_until_valid(
            self.action_choice_validate_fn, action_indexs, action_message
        )

        self.define_operation()

    def action_choice_validate_fn(self, index_list, message):
        action_list = index_list
        action_choice = input(message)
        if action_choice in action_list:
            return action_choice
        else:
            print("\nInvalid choice, TRY AGAIN")
            return False

    def run_until_valid(self, fn, index_list, message):
        result = fn(index_list, message)

        if not result:
            return self.run_until_valid(fn, index_list, message)

        return result

    def prodoct_choice_fn(self):
        product_index = ["1", "2", "3", "4"]
        product_message = "\n1.General 2.Perishable 3.Electronic 4.Clothing:\n"
        return self.run_until_valid(
            self.action_choice_validate_fn, product_index, product_message
        )

    def define_operation(self):
        if self.action_choice == "1":
            product_type_choice = self.prodoct_choice_fn()
            print(product_type_choice)

            # TASK
            # 1 GET PRODUCT TYPE Completed
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
