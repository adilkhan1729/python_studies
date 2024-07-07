a=int(input("enter a interger: "))
b=int(input("enter a integer"))
my_list=[]
my_list.extend([a,b])

def fibonacchi_series(a,b,my_list):
    for i in my_list:
        print(my_list[-1]+my_list[-2])
fibonacchi_series(a,b,my_list)

  
# num = int(input("enter a interger: "))    

# n1, n2 = 0, 1
# sum = 0

# if (num <= 0):
#     print("enter some number which is greater then zero")
# else: 
#     for i in range(num):
#       print(sum, end =' ' )
#       n1 = n2
#       n2 = sum
#       sum = n1 + n2