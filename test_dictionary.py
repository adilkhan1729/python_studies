my_dict={"1":"tesla","2":"toyota","3":"hundai","4":"lucid", "6": "tesla"}

print(my_dict["1"])

# print(my_dict["100"])
print(my_dict.get("1", 0)+str(1))

my_dict.update({"5":"subaro"})
print(my_dict)


print("Hi end of the program, this is executed at the end")