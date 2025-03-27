'''
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
'''
from collections import defaultdict

class Solution:
    def group_anagrams(self,strs):
        anagrams = defaultdict(list)
        
        for s in strs:
            sorted_s = ''.join(sorted(s))  # Sorting the string to use as a key
            print(sorted_s)
            anagrams[sorted_s].append(s)  # Grouping anagrams together

        return list(anagrams.values())

# Test cases
s = Solution()
print(s.group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))  # Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

