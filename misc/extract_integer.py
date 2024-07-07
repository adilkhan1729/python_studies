def extractIntegerWords(number):
      number = str(number)
      y=number.split(".")
      if len(y)==2:
            return False
      else:
            return True
print(extractIntegerWords(14.56))            