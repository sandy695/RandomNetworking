'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

'''
class Solution:
    def majorityElement(self, nums):
        count = 0
        for i in range(0,len(nums)):
            if count == 0:
                candidate = nums[i]
            if candidate == nums[i]:
                count += 1
            else:
                count -= 1

        return candidate

# Time complexity: O(n)
# Space complexity: O(1)
# What algorithm is used ? Boyer-Moore Voting Algorithm

# Test cases
s = Solution()
print(s.majorityElement([3,2,3])) # 3
print(s.majorityElement([2,2,1,1,1,2,2])) # 2
