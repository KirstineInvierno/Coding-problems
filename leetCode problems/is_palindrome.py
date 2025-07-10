def isPalindrome(s: str) -> bool:
    """Returns True if a given string is a palindroms after removing non-alphanumeric characters."""
    s = ''.join(char for char in s if char.isalnum()).lower()
    is_palindrome = s[::-1]
    
    return s == is_palindrome