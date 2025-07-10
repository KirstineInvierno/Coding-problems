from day_2 import calculate_horizontal, calculate_depth

def test_calculate_horizontal_valid_1():
    assert calculate_horizontal(["forward 2","down 3","forward 5"]) == 7

def test_calculate_horizontal_no_forward():
    assert calculate_horizontal(["up 2","down 3","down 5"]) == 0

def test_calculate_horizontal_valid_2():
    assert calculate_horizontal(["forward 2","forward 4","forward 10"]) == 16

def test_calculate_depth_up():
    assert calculate_depth(["down 43", "up 7", "up 9"]) == 27

def test_calculate_depth_down():
    assert calculate_depth(["down 8", "down 10", "down 20"]) == 38

def test_calculate_depth_mixed():
    assert calculate_depth(["down 35", "up 20", "down 14"]) == 29
