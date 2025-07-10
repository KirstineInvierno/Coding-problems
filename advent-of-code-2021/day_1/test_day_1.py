from .day_1 import str_to_int, count_increases, sliding_window

def test_str_to_int_valid_1():
    assert str_to_int(["1","2","3"]) == [1,2,3]

def test_str_to_int_valid_2():
    assert str_to_int(["400", "274", "2947"]) == [400,274,2947]

def test_count_increases_valid_1():
    assert count_increases(["400", "274", "2947"]) == 1

def test_count_increases_valid_2():
    assert count_increases(["1", "3", "2", "4", "0", "1"]) == 3

def test_sliding_window_valid_1():
    assert sliding_window([1, 3, 2, 4, 0, 1]) == 1

def test_sliding_window_valid_2():
    assert sliding_window([43, 84, 21, 4, 8, 28]) == 1