def read_csv():
    with open("input.txt") as f:
        return f.readlines()
    
def get_frequency():
    resulting_frequency = 0
    seen = set()
    data = read_csv()

    while True:
        for number in data:
            number = int(number)
            resulting_frequency += number
            if resulting_frequency in seen:
                return resulting_frequency
            seen.add(resulting_frequency)


        
print(get_frequency())