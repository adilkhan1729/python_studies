def multiply(list_n):
    product = 1
    for item in list_n:
        product = product *item
    return product

x = multiply([2,3,4,5])
print(x)