'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
'''

class Solution:
    def maxArea(self, height):
        min_height = 0
        max_output = 0
        n = len(height)-1
        i = 0
        while(i<n):
            min_height = min(height[i],height[n])
            x_axis = n-i
            current_output = x_axis * min_height
            if(current_output > max_output):
                max_output = current_output
            if(height[i]<height[n]):
                i+=1
            else:
                n-=1
        return max_output

# Time complexity: O(n)
# Space complexity: O(1)
# What algorithm is used ? Two pointer approach

# Test cases
s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7])) # 49
print(s.maxArea([1,1])) # 1