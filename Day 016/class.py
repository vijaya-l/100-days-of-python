# Learn about class has object and attribute


class User:
    def __init__(self, user_id, username):
        self.self_id = user_id
        self.username = username


user_1 = User("001", "vijaya")
print(user_1.self_id)
