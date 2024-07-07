num=10
n=10
for i in range(1,n+1):
    # print(i)
    # print(i*i)
    p = i*i
    # print(f"The value of p is {p} and i={i}")
    if p > num:
        print(i-1)
        break

