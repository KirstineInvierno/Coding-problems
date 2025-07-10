def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.readlines()


report = read_input("input.txt")

def str_to_int(report)-> list[int]:
    for i in range(len(report)):
        report[i] = int(report[i])
    return report


def count_increases(report)->int:
    count = 0

    for i in range(1, len(report)):
        if report[i] >= report[i-1]:
            count+=1
        else:
            count+=0
    return count

def sliding_window(report:list[int])->int:
    str_to_int(report)
    window_sum = sum(report[:3])
    total = window_sum
    count = 0
    for i in range(3, len(report)):
        window_sum += report[i] - report[i - 3]
        if window_sum > total: 
            total = window_sum
            count += 1
        total = window_sum
    return count


if __name__ == "__main__":
    report = read_input("input.txt")
    report_int = str_to_int(report)
    count_increases(report_int)
    sliding_window(report_int)
