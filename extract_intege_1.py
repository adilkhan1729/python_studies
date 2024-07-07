s = "1: Shakil, 2: zareen, 3:Adil, 4:Aaoll" 

# 1: Prakhar Agrawal, 2: Manish Kumar Rai, 3: Rishabh Gupta56

def extractIntegerWords(s):
      data = []
      new_list_data = []
      s = s.split(",")
      # print(f"s--------- is {s}")
      for item in s:
            # item.split(":")
            new_list_data.extend(item.split(":"))

      print(f"new list data is {new_list_data}")
      for item in new_list_data:
            if item.strip().isdigit():
                  data.append(item)
            # else:
            #       start_digit = 0
            #       end_digit = 0
            #       for i in range(0, len(item)):
            #             if item[i].isdigit():
            #                   start_digit = i
            #             else:
            #                   end_digit = i
            #       data.append(item[start_digit: end_digit])            
      return data    

def get_integer_from_string(s):
      start_digit = 0
      end_digit = 0
      for i in range(0, len(s)):
            if s[i].isdigit():
                  start_digit = i
            else:
                  end_digit = i
      print(f"{start_digit} {end_digit}")

get_integer_from_string("Rishabh Gupta56")

# print(extractIntegerWords("1: Prakhar Agrawal, 2: Manish Kumar Rai, 3: Rishabh Gupta56"))