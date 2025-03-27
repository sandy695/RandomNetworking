'''
Contains Duplicate
Solved 
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Input: nums = [1, 2, 3, 3]

Output: true
'''

class Solution:
    def hasDuplicate(self, nums) -> bool:
        hash_nums = {}
        for elem in nums:
            if elem in hash_nums.keys():
                return True
            else:
                hash_nums[elem] = elem
        return False

# Time complexity: O(n)
# Space complexity: O(n)
# What algorithm is used ? Hashing

# Test cases
s = Solution()
print(s.hasDuplicate([1, 2, 3, 3]))  # Output: True
print(s.hasDuplicate([1, 2, 3]))  # Output: False
