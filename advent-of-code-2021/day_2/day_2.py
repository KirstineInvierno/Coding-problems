def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.readlines()
    
report = read_input("input.txt")


def get_position(report:list[str])-> int:
    """Calculates final horizontal position"""
    horizontal = 0
    depth = 0
    for row in report:
        direction = row.split()
        number = int(direction[-1])
        if "forward" in direction:
            horizontal += number
        if "down" in direction:
            depth += number
        if "up" in direction:
            depth -= number
    return horizontal * depth


if __name__ == "__main__":
    position = get_position(report)

