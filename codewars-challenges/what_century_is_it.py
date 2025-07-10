def what_century(year:str)->str:
    """Return the century of the input year."""
    year = int(year)
    century = (year // 100) +1
    if str(year)[-2:] == "00":
        century = year // 100
        
    century = str(century)
    century_string = ""
    
    if century[0] == "1":
        century_string += century + "th"
    elif century[-1] == "1":
        century_string += century + "st"
    elif century[-1] == "2":
        century_string += century + "nd"
    elif century[-1] == "3":
        century_string += century + "rd"        
    else:
        century_string += century + "th"
    return century_string