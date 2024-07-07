print("welcome to the tip calculator")
bill=float(input("what was the total bill"))
print(bill)
percentage=float(input("please enter what is the tip percent you want to give:"))
print(percentage)
tip=(bill*percentage)/100
bill= bill+tip
split=float(input("how many people you want to split it to"))
each_person=bill/split
print("each person should pay:",each_person)