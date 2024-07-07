#User function Template for python3
class Solution:

    def valueEqualToIndex(self,arr, n):
        my_list=[]
	    
        for i in range(1, n+1):
            print(f"i={i} arr={arr[i-1]}")
            if i == arr[i-1]:
                my_list.append(i)
        return my_list
                
		# code here

s = Solution()
print(s.valueEqualToIndex([927, 11, 758, 171, 316, 577, 228, 44, 759, 1120, 11], 11))