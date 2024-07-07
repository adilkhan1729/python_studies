sa=input("enter words please ")
var=0
for i in sa:
    if i == ' ':
        var=1
        continue
    if var==1:
        print(i.upper(),end="")
    else:
        print(i,end="")
    var=0