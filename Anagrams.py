'''
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = {}
        if (len(s) != len(t)):
            return False
        for elem in s:
            if elem in hash_s.keys():
                hash_s[elem] = hash_s[elem] + 1
            else:
                hash_s[elem] = 1
        for elem in t:
            if elem in hash_s.keys():
                hash_s[elem] = hash_s[elem] - 1
                if hash_s[elem] < 0:
                    return False
            else:
                return False
        
        for elem in hash_s.values():
            if elem != 0:
                return False
        return True
    
# Time complexity: O(n)
# Space complexity: O(n)
# What algorithm is used ? Hashing

# Test cases
s = Solution()
print(s.isAnagram("anagram", "nagaram"))  # Output: True
print(s.isAnagram("rat", "car"))  # Output: False
