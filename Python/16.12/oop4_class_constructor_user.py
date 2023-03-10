print("************************************")


class User:
    def __init__(self, u_name, u_pass):
        self.username = u_name
        self.password = u_pass
        self.isLogin = False

    def login(self, u_name, u_pass):
        if(self.username == u_name and self.password == u_pass):
            self.isLogin = True

    def logout(self):
        self.isLogin = False

    def info(self):
        print(self.username, self.password, self.isLogin)

    def play(self):
        op = int(input("enter number 0 - STOP | 1 - login | 2 - logout | 3 - info "))
        if( op == 0):
            return
        elif( op == 1 ):
            user_name = input("Enter Username")
            user_pass = input("Enter Password")
            self.login(user_name, user_pass)
        elif(op == 2):
            self.logout()
        elif(op == 3):
            self.info()
        self.play()



u1 = User('hackeru', 'hackeru123')
u1.play()


