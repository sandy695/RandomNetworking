'''
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.
'''
class Solution:
    def twoSum(self, nums, target: int):
        hash_nums = {}
        
        for i, num in enumerate(nums):
            diff = target - num
            
            if diff in hash_nums:
                return [hash_nums[diff], i]
            
            hash_nums[num] = i
            
# Time complexity: O(n)
# Space complexity: O(n)
# What algorithm is used ? Hashing

# Test cases
s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(s.twoSum([3, 2, 4], 6))  # Output: [1, 2]