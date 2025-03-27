'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

nums = [1,2,3,4]
Output: [24,12,8,6]
'''

class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        result = [1] * n
        left = [1]*n
        right = [1]*n
        for i in range(1,n):
            left[i] = left[i-1] * nums[i-1]
        for i in range(n-2,-1,-1):
            right[i] = right[i+1] * nums[i+1]
        
        for i in range(0,n):
            result[i] = left[i] * right[i]
        return result

# Time complexity: O(n)
# Space complexity: O(n)
# What algorithm is used ? Prefix and Suffix product array

# Test cases
s = Solution()
print(s.productExceptSelf([1,2,3,4])) # [24,12,8,6]
print(s.productExceptSelf([1,2,3,4,5])) # [120,60,40,30,24]



class Solution1:
    def productExceptSelf(self, nums):
        n = len(nums)
        product = 1
        result = [1]*n
        for i in range(0,n):
            product = product * nums[i]
        for i in range(0,n):
            result[i] = product // nums[i]
        return result

# Time complexity: O(n)
# Space complexity: O(n)
# What algorithm is used ? Division Algorithm

# Test cases
s = Solution1()
print(s.productExceptSelf([1,2,3,4])) # [24,12,8,6]
print(s.productExceptSelf([1,2,3,4,5])) # [120,60,40,30,24]
