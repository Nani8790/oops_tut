class chatbook:

    __user_id = 1

    def __init__(self):
        self.id = chatbook.__user_id
        chatbook.__user_id += 1
        self.__name = "default user"
        self.username = ""
        self.password = ""
        self.loggedin = False
        # self.menu()

    @staticmethod
    def get_id():
        return chatbook.__user_id
    
    @staticmethod
    def set_id(value):
        chatbook.__user_id = value
        return chatbook.__user_id


#getter and setter
    def get_name(self):
        return self.__name
    

    def set_name(self, value):
        self.__name = value



    
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
            self.write_a_post()
        elif user_input == "4":
            self.send_message()
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

    
    def write_a_post(self):
        if self.loggedin == True:
            txt = input("enter your message here -->")
            print(f"content has been posted -- > {txt}")
        else:
            print("sign in first to post something")
        print("\n")
        self.menu()
    
    def send_message(self):
        if self.loggedin == True:
            txt = input("enter your message here ->")
            frnd = input("who to send the message? -- > ")
            print(f"message has been sent to --> {frnd}")
        else:
            print("please login or create a account to send message")

        print("\n")
        self.menu()


# obj = chatbook()
