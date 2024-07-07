my_list=["tesla", "tesla", "toyota", "hundai", "lucid", "tesla","toyota", "toyota","tesla"]

# {
#     "tesla" : 1+1,
#     "toyota" :1+1+1,
#     "hindai":1,
#     "lucid":1,
# }

my_dict= {}
for item in my_list:
    my_dict[item] = my_dict.get(item, 0) +1

max_k = ""
max_v = 0

for k,v in my_dict.items():
    if v > max_v:
        max_v = v
        max_k = k

print(max_k,  "===", max_v)


