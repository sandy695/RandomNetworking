'''
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
nums = [2,3,1,1,4]
[3,2,1,0,4]

'''

class Solution:
    def canJump(self, nums):
        maxreach = 0
        for index in range(len(nums)):
            if maxreach < index:
                return False
            maxreach = max(maxreach, index + nums[index])
            if maxreach >= len(nums) - 1:
                return True


# Time complexity: O(n)
# Space complexity: O(1)

# Test cases
s = Solution()
print(s.canJump([2,3,1,1,4])) # True
print(s.canJump([3,2,1,0,4])) # False
