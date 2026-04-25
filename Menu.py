from RegistrationForm import RegistrationForm
from LoginForm import LoginForm


class Menu:

    state = ""

    def __init__(self):
        self.show_menu()

    def show_menu(self):
        print("\n===== QuickMart =====\n\n1.Register  2.Login  3.Exit")
        choice = input("\nEnter choice: ")

        if choice == "1":
            self.register_login(RegistrationForm)
        elif choice == "2":
            self.register_login(LoginForm)
        elif choice == "3":
            print("Exit")
        else:
            print("Wrong")

    def register_data(self):
        # print("Register")
        username = input("Username: ")
        password = input("Password: ")
        print("\n")
        return {username, password}

    def register_login(self, fn):
        username, password = self.register_data()

        f1 = fn(username, password)
        result = f1.flow()
        if not result:
            print("\n--TRY AGAIN--")
            self.register_login(fn)

    # def register_fn(self):
    #     username, password = self.register_data()

    #     r1 = RegistrationForm(username, password)
    #     result = r1.flow()

    #     if not result:
    #         print("\n--TRY AGAIN--")
    #         self.register_fn()

    # def login_fn(self):
    #     username, password = self.register_data()
    #     l1 = LoginForm(username, password)

    #     result = l1.flow()

    #     if not result:
    #         print("\n--TRY AGAIN--")
    #         self.login_fn()


m1 = Menu()
