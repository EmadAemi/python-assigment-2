import random
a = 6
while a==6:
    order = input("Enter d to Dice! ")
    if order=='d':
        a = random.randint(1,6)
        print(a)
    else:
        print("Wrong order")
