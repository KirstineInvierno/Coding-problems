def find_uniq(arr:list):
    """Returns the odd one out from a given list."""
    counter = {}
    
    for num in arr:
        counter[num] = counter.get(num, 0) + 1
    
    for n, value in counter.items():
        if value == 1:
            return n