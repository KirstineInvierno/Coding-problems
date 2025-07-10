def expanded_form(num:int)-> str:
    expanded = ""

    if num < 10:
        return str(num)
    else:
        num = str(num)
        for i in range(len(str(num))):
            if num[i] != "0":
                if len(expanded) > 0:
                    expanded += " + "
                expanded += num[i] + "0" * (len(num) - i - 1)
    return expanded