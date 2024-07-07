import random

list1=[]
def evenchoice():
   for i in range(0,10,2):
      list1.append(i)
      print(list1)
   a=list1
   a=random.choice(list1)
   print(a)
      
list2=[]
def oddchoice():
   for e in range(1,10,2):
      list2.append(e)
      print(list2)
   b =list2
   b =random.choice(list2)
   print(b)
print("welcome to number generator")
choice=input("from which series would you like to choose your random number press1 for even series press2 two for odd series")
if choice=="press1":
   evenchoice()
elif choice=="press2"  :
   oddchoice()




      