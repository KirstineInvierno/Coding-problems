def solution(s:str)->list:
    """Returns a list of strings which are pairs of a given string."""
    if len(s) % 2 != 0:
        s += "_"
    
    pairs = []
    for i in range(0, len(s), 2):
        pairs.append(s[i:i+2])
    return pairs