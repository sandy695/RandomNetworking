'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

class Solution:
    def longestCommonPrefix(self, strs):
        prefix = strs[0]
        for elem in strs[1:]:
            while elem[:len(prefix)] != prefix and prefix:
                prefix =  prefix[:len(prefix)-1]
            if not prefix:
                break
        return prefix

# Time complexity: O(n*m) where n is the number of strings and m is the length of the longest string
# Space complexity: O(1)
# What algorithm is used ? Two pointer algorithm
# Test cases
s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"])) # "fl"
print(s.longestCommonPrefix(["dog","racecar","car"])) # ""


