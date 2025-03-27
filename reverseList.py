'''
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
'''

def reverse_words(s: str) -> str:
    words = s.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

# Time complexity: O(n) where n is the length of the input string
# Space complexity: O(n)
# What algorithm is used ? Split and reverse

# Test cases
print(reverse_words("the sky is blue"))  # Output: "blue is sky the"
print(reverse_words("  hello world  "))  # Output: "world hello"
print(reverse_words("a good   example"))  # Output: "example good a"