
def check_prime(num):
    for i in range(2,num):
        if num%i==0:
            print(f"the number {num} is not prime") 
            return
    print(f"the number {num} is_prime")    
    return
    
range1=int(input("Please enter the first range "))
range2=int(input("Please enter the second range "))
for i in range(range1,range2+1):
    check_prime(i)




# is_prime=True
# num=int(input("enter a number"))
# def check_prime(num):
#     for i in range(2,num):
#         if num%i==0:
#             return is_prime==False
#             break
#         else:
#             print(is_prime)    
#             break
# print(check_prime(num))