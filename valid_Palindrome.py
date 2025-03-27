'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
'''

def is_palindrome(s: str) -> bool:
    filtered = []
    for char in s:
        if char.isalnum():
            filtered.append(char.lower())
    filtered_str = ''.join(filtered)
    if filtered_str == filtered_str[::-1]:
        return True
    else:
        return False

# Time complexity: O(n) where n is the length of the input string
# Space complexity: O(n)
# What algorithm is used ? Two-pointer technique

# Test cases
print(is_palindrome("A man, a plan, a canal: Panama"))  # Output: True
print(is_palindrome("race a car"))  # Output: False
print(is_palindrome(" "))  # Output: True

