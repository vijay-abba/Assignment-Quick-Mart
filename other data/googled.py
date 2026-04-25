# 1.How to hash Password

# 2. How to search for *.txt files  and get data form it 



# DOUBT
    def user_exist(self):
        files = list(Path("").glob("*.txt"))
        found_user = False
        for i in files:
            file_name = str(i).split(".")[0]

            if file_name == self.username:
                print("User EXIST")
                found_user = True
        else:
            print("No user found")
            found_user = False
        


# Doubt 2 (CLEARED )
    def register_data(self):
        # print("Register")
        username = input("Username: ")
        print("userName ENTERE : ", username)
        password = input("Password: ")
        print("password ENTERE : ", password)
        print("\n")
        return {username, password} # it it wont' pack to {username: username} like JS ? 
                                    # printing it {"vijay", "password"} is it dict? 
                                    # it is set 

    def register_login(self, fn):
        data = self.register_data()
        print(data)

        username, password = data

        print("usernaem: ",username)
        print("password: ",password)
        f1 = fn(username, password)
        result = f1.flow()
        print(result)
        if not result:
            print("\n--TRY AGAIN--")
            self.register_login(fn)