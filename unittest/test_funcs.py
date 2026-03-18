# TODO: 사용자 모듈 import
from my_funcs import is_even, get_average, get_max, get_min

# TODO: 아래의 코드를 삭제하고 unittest를 작성하세요.
def test_my_first_testcase():
    l = [1, 2, 3, 4, 5]
    assert l == [1, 2, 3, 4, 5]

def test_is_even():
    assert is_even(4) is True
    assert is_even(7) is False
    assert is_even(0) is True

def test_get_average():
    sample_list = [1, 2, 3, 4, 5]
    assert get_average(sample_list) == 3.0
    assert get_average([10, 20, 30]) == 20.0

def test_get_max():
    assert get_max([1, 9, 5, 3]) == 9
    assert get_max([-10, -2, -5]) == -2

def test_get_min():
    assert get_min([1, 9, 5, 3]) == 1
    assert get_min([100, 200, 50]) == 50