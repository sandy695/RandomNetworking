'''
we start at the beginning of the list using i and keep track of the current element.
We iterate next elements using j and check if j not equal to I
if so, we do i+1 and replace i with j
'''

class Solution:
    def removeDuplicates(self, num):
        i = 0
        for j in range(1,len(num)):
            if num[j] != num[i]:
                i += 1
                num[i] = num[j]
        return i+1  
# Time complexity: O(n)
# Space complexity: O(1)
# What algorithm is used ? Two pointer algorithm

# Test cases
s = Solution()
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4])) # 2
