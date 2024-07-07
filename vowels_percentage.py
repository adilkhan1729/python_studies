# count=0.0
# sentence=(input("enter a sentence : "))
# for i  in   sentence:
#     if i=="a" or i== "e" or i== "i" or i=="o" or i=="u":
#         count=count+1
# percent=(count*100/len(sentence))
# print(percent)      

count=0.0
vowels=["a","e","i","o","u"]
sentence=(input("enter a sentence : "))
for i  in   sentence:
    if i in vowels:
        count=count+1
percent=(count*100/len(sentence))
print(percent)        


# count=0.0
# vowels=["a","e","i","o","u"]
# sentence=(input("enter a sentence : "))
# for i  in   sentence:
#     if i not in vowels:
#         count=count+1
# percent=(count*100/len(sentence))
# print(percent)   

