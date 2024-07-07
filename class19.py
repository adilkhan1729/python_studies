def myfunc(mylist):
    # global mylist
    print("\t list received",mylist)
 
    mylist.extend([7,1])
    # mylist.remove(7)
    print("\t list within called fuction",mylist)
    print(mylist)

list1=[1]
print("list before funcrtion call:",list1)
myfunc([list1])
print("\t list after function call:",list1)
