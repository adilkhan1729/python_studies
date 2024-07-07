    def countSquares(self, N):
        count=0
        # list_number = [x for x in range(1,N)]
        for i in range(1,N//2):
            if sqrt(i) < N:
                count += 1
        return count


# import math
# x = math.sqrt(5) - math.floor(math.sqrt(5))
      2.34        -  2.0        
# if x == 0:
#     print(f" is a perfect square")
# else:
#     print(f"x is a not perfect square")

import math
# y = math.sqrt(4)
# x = math.floor(math.sqrt(4))
# print(y)
# print(x)

x = int(math.sqrt(5))
print(x)