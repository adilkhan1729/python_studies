print("welcome to the roller coaster")
photo=input("do you want a photo yes or no ")
bill=0

if photo == "yes":
    bill = 3
else:
    bill  = 0    
age=int(input("what is your age please "))
height=int(input("what is your height in cm "))
if height>=120:
    print("you can ride the rollor coaster")
    if age<12:
        bill=+ 5
        print(f"you have to pay {bill} for ride")
    elif  age<=18:
        bill += 7  
        print(f"youth you have to pay {bill} for ride")    
    else:
        bill += 12
        print(f" adult you have to pay {bill} for ride")    
else:
    print("you can't go sorry")    