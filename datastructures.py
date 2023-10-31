#tuples
names = ("Hadassa","Praise","Michael","Moses","James","Elvis")

print(names[1])
print(names[2])
print(names)
print(names[1:4])
print(names[2:])
# names [o] = mwende this is not possible

# lists
cars = ["mercedes", "audi", "lamborgini"]
print(cars[1])
print(cars[2])
cars.append("jeep")
print(cars)
print(cars[1:4])
print(cars[2:])
cars[0] = "mercedes benz"  # this is possible
print(cars[0])

# dictionaries
students = {"ADM1": "Torry", "ADM2": "Precious"}
print(students["ADM1"])
print(students)

#sets
numbers = {1, 2, 3, 4, 5, 6, 7,8,9,1,2,3,4,5}
print(numbers)