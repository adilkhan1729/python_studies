height=float(input("please enter the height in meter "))
weight=float(input("please enter your weight in KG "))
bmi=weight/(height*height)
print("Your BMI is ", bmi)
if bmi<18.5:
    print("you are underweight")
elif bmi>18.5 and bmi<25:
    print("you are normal weight")
elif bmi>25 and bmi<30:
    print("you are overweight")
elif bmi>30 and bmi<35:
    print("obese")
else:
    print("clinically obese")
            

