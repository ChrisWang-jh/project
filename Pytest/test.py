def test_ok():
    open("main.py")
    assert 1 ==1

def test_fail():
    assert False

a = 123
b = test_ok
test_b = test_ok
