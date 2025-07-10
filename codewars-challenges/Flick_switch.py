def flick_switch(lst: str) -> list[bool]:
    flick = True
    bool_list = []
    for word in lst:
        if word == "flick":
            flick = not flick
        bool_list.append(flick)
    return bool_list
