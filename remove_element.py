'''
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
'''
'''
Two pointer algorithm
traverse the list using i and j where both are equal to 0
When i not equal to val, nums[j] becomes nums[i] and keep incrementing i
return j
'''

class Solution:
    def removeElement(self, nums, val):
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j
    
# Time complexity: O(n)
# Space complexity: O(1)
# What algorithm is used ? Two pointer algorithm

# Test cases
s = Solution()
print(s.removeElement([3,2,2,3], 3)) # 2
print(s.removeElement([0,1,2,2,3,0,4,2], 2)) # 5