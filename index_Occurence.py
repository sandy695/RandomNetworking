'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        needle_len = len(needle)
        haystack_len = len(haystack)
        
        for i in range(haystack_len - needle_len + 1):
            if haystack[i:i + needle_len] == needle:
                return i
        return -1

# Time complexity: O(n * m) where n is the length of haystack and m is the length of needle
# Space complexity: O(1)
# What algorithm is used ? Sliding window algorithm

# Test cases
s = Solution()
print(s.strStr("sadbutsad", "sad"))  # Output: 0
print(s.strStr("leetcode", "leeto"))  # Output: -1