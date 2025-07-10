def string_expansion(s:str)->str:
    multiplier = 1
    expanded = ""
    
    for char in s:
        if char.isdigit():
            multiplier = int(char)
        if char.isalpha():
            expanded += (multiplier * char)
    return expanded