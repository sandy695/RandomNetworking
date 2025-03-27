'''
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.
[3,0,6,1,5]
[6,5,4,3,0]

[1,3,1]
[3,1,1]
'''

class Solution:
    def hIndex(self, citations):
        h = 0
        citations.sort(reverse = True)
        for i in range(0,len(citations)):
            if(i+1 > citations[i]):
                break
            else:
                h +=1
        return h
    
# Time complexity: O(nlogn)
# Space complexity: O(1)
# What algorithm is used ? Sorting, greedy algorithm

# Test cases
s = Solution()
print(s.hIndex([3,0,6,1,5])) # 3
print(s.hIndex([1,3,1])) # 1
print(s.hIndex([3,0,6,1,5])) # 3