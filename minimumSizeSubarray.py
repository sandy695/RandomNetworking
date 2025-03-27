'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
'''

class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        n = len(nums)
        left = 0
        current_sum = 0
        min_length = float('inf')
        
        for right in range(n):
            current_sum += nums[right]
            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                print("min_length", min_length)
                current_sum -= nums[left]
                print("current_sum", current_sum)
                left += 1
        
        return min_length if min_length != float('inf') else 0
    
# Time complexity: O(n)
# Space complexity: O(1)
# What algorithm is used ? Sliding window (two-pointer) technique

# Test cases
s = Solution()
print(s.minSubArrayLen(7, [2,3,1,2,4,3]))  # Output: 2
