def is_pangram(st:str)->bool:
    """Returns True if a given string is a pangram."""
    letters = set()
    for letter in st.lower():
        if letter.isalpha():
            letters.add(letter)
    if len(letters) >= 26:
        return True
    return False