class Fruit:
    def __init__(self, name, size, price):
        self.name = name
        self.size = size
        self.price = price

class Flower:
    def __init__(self, name, price, state):
        self.name = name
        self.price = price
        self.state = state


class Car:
    def __init__(self, name, color, model, debut):
        self.name = name
        self.color = color
        self.model = model
        self.debut = debut

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    def register(self):
         print("yeah I can register")


    def login(self):
        print("yeah I can login")

class Admin(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.name = name
        self.email = email
        self.password = password

    def suspendUser(self):
        print("yeah i can suspend users")

