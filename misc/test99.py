
def swap_elements():
    number = (input("enter a few numbers")) 
    number.split(" ")           
    number=list(number) 
    number[0],number[-1]=number[-1],number[0]
    return number
swap_elements()