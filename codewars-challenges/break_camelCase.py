def solution(s:str)->str:
    """Breaks up a given string using camel casing."""
    spaced = ""
    for char in s:
        if char.isupper():
            spaced += " " + char
        else:
            spaced += char
    return spaced