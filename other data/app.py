


# Login and Registration
class Person:

    def __init__(self, username, password):
        pass

    def check_username():
        pass

    def check_password():
        pass

    def hash_password():
        pass

    def save_user():
        pass


class Staff(Person):

    def __init__(self, username, password):
        print(username, password)


p1 = Staff("vijay", "1234")
print(p1)


def register():
    username = input("Username: ")
    password = input("Password: ")

    print(username)
    print(password)

def login():
    username = input("Username: ")
    password = input("Password: ")
    print(username)
    print(password)

def initial():
    print("\n\n===== QuickMart =====")
    choice = input("1.Register  2.Login  3.Exit \n Enter choice: ")

    if(choice == "1"):
        print("\n--- Register ---")
        register()
    elif(choice == "2"):
        print("\n--- Login ---")
        login()
    elif(choice == "3"):
        print("\n--- Exit ---")
    else:
        print("\n\nYou have Entered Wrong input TRY AGAIN")
        initial()

initial()