str = "this is hello world hello for this perioed of time in the world"
l = str.split()
var1 = []

for item in l:
    if item not in var1:
        var1.append(item)

print(var1)

# Convert list to string
new_str = ""
for i in var1:
    new_str += i + " "

print(new_str)