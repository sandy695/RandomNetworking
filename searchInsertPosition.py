'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
'''
'''
Binary search
Start with 2 var left and right, when left is less than right iterate through the list
Find the mid and check if the mid is equal to target or less than target or greater than target
If mid is equal to target return mid
If mid is less than target increment left
If mid is greater than target decrement right
Return left

1,3,5,6
'''
class Solution:
    def search_insert_position(self,nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left
    
# Time complexity: 0 (log n)
# Space complexity: O(1)

# Example usage
s = Solution()
nums = [1, 3, 5, 6]
target = 5
print(s.search_insert_position(nums, target))  # Output: 2

target = 2
print(s.search_insert_position(nums, target))  # Output: 1

target = 7
print(s.search_insert_position(nums, target))  # Output: 4

target = 0
print(s.search_insert_position(nums, target))  # Output: 0