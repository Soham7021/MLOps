class chatbook:

    __user_id = 0

    def __init__(self):
        self.__name = "Default name" # encapsulated or hidden from the other users
        chatbook.__user_id += 1
        self.username = ""
        self.password = ""
        self.logged_in = False
        self.menue()

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

    def menue(self):
        print("""
        Welcome to Chatbook!
        1. Sign Up
        2. Sign In
        3. write a post
        4. messg frnd
        5. Exit
    """)
        print(" ")
        choice = input("Enter your choice: ")
        if  choice == "1" :
            self.sign_up()
        elif choice == "2" :
            self.sign_in()
        elif choice == "3" :
            self.write_post()
        elif choice == "4" :
            self.messg_frnd()
        else:
            exit()

    def sign_up(self):
        self.username = input("Enter your username: ")
        self.password = input("Enter your password: ")
        print("Sign up successful!")
        self.menue()

    def sign_in(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username == self.username and password == self.password:
            self.logged_in = True
            print("Sign in successful!")
        else:
            print("Invalid credentials or Sign up first.")
        self.menue()

    def write_post(self):
        if not self.logged_in:
            print("You must be logged in to write a post.")
            self.menue()
            return
        post = input("Enter your post: ")
        print("Post published!")
        self.menue()

    def messg_frnd(self):
        if not self.logged_in:
            print("You must be logged in to message a friend.")
            self.menue()
            return
        friend = input("Enter your friend's username: ")
        message = input("Enter your message: ")
        print(f"Message sent to {friend}!")
        self.menue()

app = chatbook()