def move_zeros(lst:list)->list:
    """Moves all zeros of a given array to the end, preserving the order of other elements."""
    zero_list = []
    non_zero_list = []
    
    for i in lst:
        if i == 0:
            zero_list.append(i)
        else:
            non_zero_list.append(i)
    
    final = non_zero_list + zero_list
    return final