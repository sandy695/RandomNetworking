'''
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
'''

class Solution:
    def reverse(self,i,j,nums):
        while i < j:
            nums[i],nums[j] = nums[j],nums[i]
            i += 1
            j -= 1
            
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        self.reverse(0,n-1,nums)
        self.reverse(0,k-1,nums)
        self.reverse(k,n-1,nums)
        print(nums)
        
# Time complexity: O(n)
# Space complexity: O(1)
# What algorithm is used ? Reversal Algorithm

# Test cases
s = Solution()
print(s.rotate([1,2,3,4,5,6,7], 0)) # [5,6,7,1,2,3,4]
