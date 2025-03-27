'''
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.
'''
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums, k: int):
        final_l = []
        count_d = defaultdict(int)
        for elem in nums:
            count_d[elem] += 1
        
        count_l = [[]for i in range(len(nums)+1)]

        for index, values in count_d.items():
            count_l[values].append(index)
        
        for i in range(len(count_l)-1,0,-1):
            for elem in count_l[i]:
                final_l.append(elem)
                if(len(final_l) == k):
                    return final_l

# Time complexity: O(n)
# Space complexity: O(n)
# What algorithm is used ? Bucket sort
# What data structure is used ? List, Dictionary

# Test cases
s = Solution()
print(s.topKFrequent([1,1,1,2,2,3], 2)) # [1,2]
print(s.topKFrequent([1], 1)) # [1]
print(s.topKFrequent([1,2], 1)) # [1]