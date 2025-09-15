def longest_palindromic_substring(s: str) -> str:
    if len(s) == 0:
        return ""
    
    # Function to expand around the center and return the longest palindrome
    def expand_from_center(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Return the palindrome substring (excluding the last expansion that broke the palindrome)
        return s[left + 1:right]
    
    longest = ""
    
    for i in range(len(s)):
        # Odd-length palindromes (expand around a single character)
        odd_palindrome = expand_from_center(i, i)
        # Even-length palindromes (expand around a pair of characters)
        even_palindrome = expand_from_center(i, i + 1)
        
        # Check if the found palindrome is the longest
        if len(odd_palindrome) > len(longest):
            longest = odd_palindrome
        if len(even_palindrome) > len(longest):
            longest = even_palindrome
    
    return longest

# Example usage
input_str = "bharat"
print(f"Longest palindromic substring: {longest_palindromic_substring(input_str)}")