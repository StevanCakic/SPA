class User:
    def __init__(self):
        print("User init")
    def who_am_i(self):
        print("I'm User")
    def login(self):
        print("User login")

class Admin(User):
    def __init__(self):
        User.__init__(self)
        print("Admin")
    def who_am_i(self):
        print("I'm Admin")
    def delete_user(self):
        print("I can delete User")
    
user1 = User()
print("----------")
admin1 = Admin()
print("----------")
user1.who_am_i()
print("----------")
admin1.who_am_i()
print("----------")
admin1.login()
print("----------")
