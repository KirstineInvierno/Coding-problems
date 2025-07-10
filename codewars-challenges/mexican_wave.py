def wave(people:str)->list[str]:
    """Returns a list of elements that represent a mexican wave."""

    return [people[:i] + people[i].upper() + people[i+1:] for i, letter in enumerate(people) if letter != " "]