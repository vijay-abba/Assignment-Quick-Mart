


class LoginAndRegistrationForm:

    def __init__(self):
        print("\n\n===== QuickMart =====")
        choice = input("1.Register  2.Login  3.Exit \n Enter choice: ")
        
        if (choice=="1"):
            self.register()
        elif (choice=="2"):
            self.login()
        elif (choice == "3"):
            print("Exit")
        else:
            print("You Have Entred a Wrong Input \n TRY AGAIN !")
            self.__init__()


    def register(self):
        print("--- Register ---")
        username = input("Username: ")
        password = input("Password: ")
        print(username, password)

    def validate_username(self):


    def login(self):
        print("--- Login ---")

    
    


    



lr1 = LoginAndRegistrationForm()
