def is_float(n):
    try:
        float(n)
        return True
    except ValueError:
        return False


calculator=(input("what do you want to use we have + - * / "))
if calculator in ("+","-","*","/"):
    number1=input("enter your number ")
    number2=input("enter your number ")

    if  number1.isdigit()  or is_float(number1):
        number1 = float(number1)
        if number2.isdigit() or is_float(number2):
            number2 = float(number2)
            if calculator=="+":
                print(f"so your answer is {round(number1+number2,2)} ")
            if calculator=="-":
                print(f"so your answer is {round(number1-number2,2)} ")  
            if calculator=="*":
                print(f"so your answer is {round(number1*number2,2)} ")
            elif calculator=="/":
                print(f"so your answer is {round(number1/number2,2)} ")
        else:
            print("Second number isd not a digit")
    else:
        print("Please enter the numeric value only")
    
else:
    print("we don't know what you are talking about")
