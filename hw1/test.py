import myfile

def test_correct():
    assert myfile.add(1, 1) == 2

def test_incorrect():
    assert myfile.add(2, 3) == 4