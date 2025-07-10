def pyramid(n: int) -> list:
    """Returns an array of n ascending length subarrays, all filled with 1s."""
    list_of_ones = []

    for i in range(1, n+1):
        sublist = [1] * i
        list_of_ones.append(sublist)
    return list_of_ones