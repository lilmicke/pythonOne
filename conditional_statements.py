age = 17
bribe = 900
vipAmount = 1500
if age < 18:
    if bribe < 1000:
        print("go home")
    else:
        print("use gate b")
else:
    if vipAmount >= 1500:
        print("please go to vip")
    else:
        print("welcome to the party")



marks = 90
if marks < 40:
            print("E")
elif marks < 50:
            print("D")
elif marks < 60:
            print("C")
elif marks < 70:
            print("B")
else:
            print("A")