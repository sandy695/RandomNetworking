'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

class Solution:
    def two_Sum(self, nums, target):
        # create Dictionary
        two_sum_dict = {}
        # iterate through the list
        for i in range(len(nums)):
            diff = target - nums[i]
            # check if the difference is in the dictionary
            if diff in two_sum_dict:
                return [two_sum_dict[diff], i]
            # add the element to the dictionary
            else:
                two_sum_dict[nums[i]] = i
        return []
# Time complexity: O(n)
# Space complexity: O(n)

# Test cases
s = Solution()
print(s.two_Sum([5,2, 7, 11, 15], 9)) # [0, 1]
    
            
