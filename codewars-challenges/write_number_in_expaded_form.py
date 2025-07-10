def expanded_form(num:int)->str:
    """Returns a string of a number in expanded form."""
    expanded = []
    num = str(num)

    for i in range(len(num)):
        if num[i] != "0":
            value = int(num[i]) * (10 ** (len(num) - i - 1))
            expanded.append(str(value))
    return " + ".join(expanded)