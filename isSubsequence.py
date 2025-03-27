class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_index = 0
        t_index = 0
        s_len = len(s)
        t_len = len(t)
        while(s_index < s_len and t_index < t_len):
            if(s[s_index] == t[t_index]):
                s_index +=1
            t_index += 1
        if(s_index == s_len):
            return True
        else:
            return False

# Time complexity: O(n + m) where n is the length of s and m is the length of t
# Space complexity: O(1)
# What algorithm is used ? Two-pointer technique

# Test cases
s = Solution()
print(s.isSubsequence("abc", "ahbgdc"))  # Output: True
print(s.isSubsequence("axc", "ahbgdc"))  # Output: False
print(s.isSubsequence("", "ahbgdc"))  # Output: True