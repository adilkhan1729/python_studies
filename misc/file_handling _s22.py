# ''' 
# file handling can do following task
# 1 create a file
# 2 read file
# 3 write to file
# '''
#  fp=open(r'/Users/adil/My Drive/adil_codeyoung/sample.txt','r')
# print(fp.read())
# fp.close()
# name=input("what is your name:  ")
# password=len(input("what is your password and it has to be greater than four"))
# if password<4:
#     print("i am sorry but you can't have a password that short")
# elif password>4:
#     print("your good to go")
# fp=open('database.txt','w')
# s=password
# fp.write(str(s))
# l=[str(name),str(password)]
# fp.writelines(l)
# fp.close()
# fp=open('database.txt','r')
# print(fp.read())
# fp.close()

database=open("database.txt","a")
database.close()
def signup():
  print()
  print("enter following datails to signup")
  print()
  username=input("enter username  :")
  if len(username)==0:
    print("usename can not be blank")
    print("please try again")
    return
  database = open("text.txt",'r')
  for data in database:
    u,p=data.split(",")
    if username ==u:
      print("username already exist")
      print("please try again")
      database.close()
      return
  database.close()
  password=input("enter your password  :")
  if len(password)<4 :
    print("password should contain more tan 4 characters")
    print("please try again")
    return
    password_c=input("enter your password again  :")
    if password !=password_c:
      print("entered password are not same. please try again.")
      return
      database=open("database.txt","a")
      record=username+","+password+"\n"
      database.write(record)
      print()
      print("signup successful")
      print()
    database.close()
def login():
  print()
  print("enter following details to login")
  print()
  username=input("enter username  :")
  database=open("database.txt",'r')
  flag=0
  for data in database:
    u,p=data.split(",")
    if username==u:
      flag=1
      print(p)
      break
  database.close() 
  if flag==0:
    print()
    print("username do not exist")
    print("please try again")

    print()
    return
  else:
    password=input("enter the password :")
    if password == input("enter the password  :"):
        if password+"\n"==p:
            print()
            print("--login successful--")
            print()
            quit()
    else:
        print()
        print("incorrect password")
        print("please try again ")
        print()
        return
while True:
  print()
  print("---welcome---")
  print()
  print("1--> singup/register")
  print("2--> login")
  print("3-->exit")
  print()
  ch=int(input("enter your choice  :"))
  if ch==1:
    signup()
  elif ch==2:
    login()
  elif ch==0:
    print("thank you")
    break
  else:
    print("invalid input")
    print("please try again")
    continue
    
