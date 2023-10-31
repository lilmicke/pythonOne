def motto():
    print("Hello there this is our motto")
motto()

def vision():
    print("Hey this is our vision")
vision()

def addition():
    x = 10
    y = 20
    z = x + y
    print("your answer is",z)
addition()

def sum(x, y):
    z = x + y
    print("your answer is",z)
sum(30, 40)
sum(50,90,)

def avg(name,firstnumber,secondnumber,thirdnumber):
    answer = (firstnumber +secondnumber+thirdnumber)/3
    print("hello",name,"your average is",answer)
avg("king",400,600,700)

def simpleInterestCal(principle,rate,time):
    interest = (principle*rate*time)/100
    return interest
print(simpleInterestCal(1000,400,5))