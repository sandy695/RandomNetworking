'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
'''

def is_subsequence(s: str, t: str) -> bool:
    s_len, t_len = len(s), len(t)
    s_index, t_index = 0, 0
    
    while s_index < s_len and t_index < t_len:
        if s[s_index] == t[t_index]:
            s_index += 1
        t_index += 1
    
    return s_index == s_len

# Time complexity: O(n + m) where n is the length of s and m is the length of t
# Space complexity: O(1)
# What algorithm is used ? Two-pointer technique

# Test cases
print(is_subsequence("abc", "ahbgdc"))  # Output: True
print(is_subsequence("axc", "ahbgdc"))  # Output: False
print(is_subsequence("", "ahbgdc"))  # Output: True
print(is_subsequence("abc", ""))  # Output: False
