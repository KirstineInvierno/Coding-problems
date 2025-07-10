def unique_in_order(sequence)->list:
    """Returns a list of items without any elements with the same value next to each other."""
    unique = []

    if len(sequence) == 0:
        return unique
    unique.append(sequence[0])
    for char in sequence:
        if char != unique[-1]:
            unique.append(char)

    return unique