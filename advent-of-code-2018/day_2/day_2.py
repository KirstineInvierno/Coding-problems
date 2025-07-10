from collections import defaultdict

def read_input():
    with open("input.txt") as file:
        return file.readlines()
    

def count_letters():
    data = read_input()
    two_count = 0
    three_count = 0
    for row in data:
        count = defaultdict(int)
        for letter in row:
            count[letter] += 1
        if 2 in count.values():
            two_count += 1
        if 3 in count.values():
            three_count += 1
    return two_count * three_count
    


# compare the first row to all the other rows
# if they differ by one character, return the characters that are the same
# if more than one character difference, get the next row

def compare_characters():
    data = read_input()
    compare = ""

    for row in data:
        compare += row
        for index, letter in enumerate(row):
            pass