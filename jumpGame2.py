
class Solution:
    def jump(self, nums):
        maxreach = 0
        jumps = 0
        maxindex = 0
        for index in range(len(nums)-1):
            maxreach = max(maxreach, index + nums[index])
            if(maxindex == index):
                jumps += 1
                maxindex = maxreach
                if maxindex >= len(nums) - 1:
                    break
        return jumps
    
# Time complexity: O(n)
# Space complexity: O(1)
# What algorithm is used ? Greedy Algorithm

# Test cases

s = Solution()
print(s.jump([2,3,1,1,4])) # 2
print(s.jump([2,3,0,1,4])) # 2
print(s.jump([2,3,0,1,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])) # 5