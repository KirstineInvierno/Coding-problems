def isAnagram(self, s: str, t: str) -> bool:
    """Returns True if t and s are anagrams."""
    s_letters = {}
    t_letters = {}

    for letter in s:
        s_letters[letter] = s_letters.get(letter,0) +1
    for char in t:
        t_letters[char] = t_letters.get(char,0) +1
    
    return s_letters == t_letters