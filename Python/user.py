

class User:
    """class User"""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"User's first name is {self.first_name}")
        print(f"User's last name is {self.last_name}")

    def greet_user(self):
        print(f"Hello to {self.first_name} {self.last_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0



class Admin(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = ["can add post",
                           "can delete post",
                           "can ban user"]

    def show_privileges(self):
        print(f"The Admin has {self.privileges}")




user1 = User("Jack", "Billy")
user1.greet_user()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)

user2 = Admin("Bob", "Cell")
user2.show_privileges()