def count_letters(seq:list[int])-> dict:
    """Returns a count of each number in a given list"""
    letter_counter = {}
    for i in range(len(seq)):
        letter_counter[seq[i]] = 0
        if seq[i] in letter_counter:
            letter_counter[seq[i]] += 1
    return letter_counter
    
def find_odd_instance(letter_counter: dict) -> int:
    """Returns an integer that appears an odd number of times."""
    for key, value in letter_counter.items():
        if value % 2 != 0:
            return key
    
if __name__ == "__main__":
    letter_counter = count_letters(seq)
    find_odd_instance(letter_counter)