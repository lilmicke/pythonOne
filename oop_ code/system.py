from file1 import *
# These are objects from a fruit class
tundaOne = Fruit("Orange", "200g", "ksh.50")
tundaTwo = Fruit("Mango", "300g", "ksh.70")
print(tundaTwo.size)


# These are objects from a flower class
ua1 = Flower("Rose", "ksh.299", "natural")
ua2 = Flower("Lily", "ksh 150", "artificial")
print(ua1.name)
print(ua2.state)

# These are objects from a car class
type1 = Car("Mazda", "red", "CX5", "2022")
type2 = Car("mercedes", "black", "C200", "2004")
print(type1.name)

# These are objects from a user class
person1 = User("Holland", "holland@gmail.com", "abcdef")
person1.register()

# These are objects from an admin class
admin1 = Admin("puff", "holland@gmail.com", "abcdef")
admin1.register()
admin1.login()
admin1.suspendUser()
