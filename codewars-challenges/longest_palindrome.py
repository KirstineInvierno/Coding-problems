def longest_palindrome (s:str)->int:
    """Returns the longest substring length in a given string that is the same in reverse."""
    longest = "" 

    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            if substring == substring[::-1]:
                if len(substring) > len(longest):
                    longest = substring
    return len(longest)