import pytest

def add(a, b):
    return a+b

def test_add_num():
    ans = add(1,3)
    assert ans == 4

def test_add_str():
    ans = add('abcd', 'efgh')
    assert ans == 'abcdefgh'

# 添加fixtrue
@pytest.fixture
def f():
    print('用例开始执行')
    yield
    print('用例结束执行')

class Testadd: # Test类本身不是用例，但是可以很好的整理用例

    def test_num(self,f):
        ans = add(1,3)
        assert ans == 4

    @pytest.mark.usefixtures('f')
    def test_str(self):
        ans = add('abcd', 'efgh')
        assert ans == 'abcdefgh'



pytest.main()