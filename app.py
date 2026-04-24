


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



def initial():

    menu = {
        "1": "--- Register ---",
        "2": "--- Login ---",
        "3": "--- Exit ---"
    }

    print("\n\n===== QuickMart =====")
    choice = input("1.Register  2.Login  3.Exit \n Enter choice: ")

    if(choice == "1"):
        print(menu["1"])
    elif(choice == "2"):
        print(menu["2"])
    elif(choice == "3"):
        print(menu["3"])
    else:
        print("\n\nYou have Entered Wrong input TRY AGAIN")
        initial()



initial()