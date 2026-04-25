

class Menu:

    state = ""
    def __init__(self):
        self.show_menu()

    def show_menu(self):
        print("\n===== QuickMart =====")
        print("\n1.Register  2.Login  3.Exit")
        choice = input("\nEnter choice: ")

        if(choice == "1"):
            print("Register")
        elif choice == "2":
            print("Login")
        elif choice == "3":
            



m1 = Menu()