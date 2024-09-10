import hw2_debugging


def test_even():
    assert hw2_debugging.merge_sort([3, 4, 2, 1, 5, 8, 9, 7, 6, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_odd():
    assert hw2_debugging.merge_sort([3, 4, 2, 1, 5, 8, 9, 7, 10]) == [1, 2, 3, 4, 5, 7, 8, 9, 10]

def test_dup():
    assert hw2_debugging.merge_sort([6, 3, 3, 4, 2, 1, 5, 8, 6, 9, 7, 10]) == [1, 2, 3, 3, 4, 5, 6, 6, 7, 8, 9, 10]