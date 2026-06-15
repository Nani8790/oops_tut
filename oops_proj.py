class chatbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.loggedin = False
        self.menu()


    
    def menu(self):
        user_input = input("""welcome to chatbook !! how would you like to proceed?"
                           1. press 1 to signup
                           2. press 2 to signin
                           3. press 3 to write to post
                           4. press 4 to message to friend
                           5. press any other number to exit\n""")
        
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()

    def signup(self):
        email = input("enter your email here! > ")
        pwd = input("enter your password! > ")
        self.username = email
        self.password = pwd
        print("Account has been created successfully")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == "" and self.password == "":
            print("please signup first by pressing 1 in the main menu")
        else:
            uname = input("enter the username/ email here! > ")
            pwd = input("enter the password here! > ")

            if self.username == uname and self.password == pwd:
                print("you have signed in successfully")
                self.loggedin =  True
            else:
                print("enter the correct credentials")
        print("\n")
        self.menu()
            


obj = chatbook()
