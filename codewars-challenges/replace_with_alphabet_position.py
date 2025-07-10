def alphabet_position(text)->str:
    """Replaces every letter of a given string with its position in the alphabet."""
    output = []
    for letter in text.lower():
        if letter.isalpha():
            value = ord(letter) - 96
            output.append(str(value))
    output_str = " ".join(output)
    return output_str