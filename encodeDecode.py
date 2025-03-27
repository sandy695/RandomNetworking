class Solution:
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        Args:
            strs: List of strings to encode
            
        Returns:
            A single string containing all encoded strings
        """
        if not strs:
            return ""
        
        # Use length#string format for each string
        return ''.join(f"{len(s)}#{s}" for s in strs)
    
    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        Args:
            s: The string to decode
            
        Returns:
            List of original strings
        """
        if not s:
            return []
        
        result = []
        i = 0
        
        while i < len(s):
            # Find the delimiter #
            j = i
            while s[j] != '#':
                j += 1
            
            # Get the length of the next string
            length = int(s[i:j])
            
            # Extract the string and add to result
            result.append(s[j + 1:j + 1 + length])
            
            # Move pointer to start of next length indicator
            i = j + 1 + length
            
        return result

# Test cases
codec = Solution()
test_cases = [
    ["neet", "code", "love", "you"],
    ["we", "say", ":", "yes"],
    [],
    ["Hello World!"]
]

for test in test_cases:
    encoded = codec.encode(test)
    decoded = codec.decode(encoded)
    print(f"Original: {test}")
    print(f"Encoded: {encoded}")
    print(f"Decoded: {decoded}")
    print(f"Match: {test == decoded}\n")