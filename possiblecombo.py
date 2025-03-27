'''
Given a string containing digits 2-9 return all letter combo that digits can represent. mapping of digits to letters is just like telephone buttons. What algo would you use, give me the code and explain it
'''

def letter_combinations(digits: str):
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    def backtrack(index, path):
        if index == len(digits):
            combinations.append(''.join(path))
            return
        possible_letters = phone_map[digits[index]]
        for letter in possible_letters:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()
    
    combinations = []
    backtrack(0, [])
    return combinations

# Time complexity: O(3^n * 4^m) where n is the number of digits that map to 3 letters and m is the number of digits that map to 4 letters
# Space complexity: O(3^n * 4^m) for storing the combinations

# Test cases
print(letter_combinations("23"))  # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(letter_combinations(""))  # Output: []
print(letter_combinations("2"))  # Output: ["a","b","c"]
