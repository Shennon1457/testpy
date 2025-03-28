from src.calc import Calculator as bas
import pytest 

calc = bas()

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (3, 5, 8),
        (6, 5, 11),
        (3, 7, 10),
        (8, 10, 18),
        (15, 4, 19)
    ]
)

def test_sum(a, b, expected):
    assert calc.sum(a, b) == expected
    
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (3, 5, -2),
        (6, 5, 1),
        (3, 7, -4),
        (18, 10, 8),
        (15, 4, 11)
    ]
)
def test_sub(a, b, expected):
    assert calc.subtract(a, b) == expected
    
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (3, 5, 15),
        (6, 5, 30),
        (3, 7, 21),
        (18, 10, 180),
        (15, 4, 60)
    ]
)
def test_mult(a, b, expected):  
    assert calc.multiply(a, b) == expected
    
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (4, 2, 2),
        (6, 1, 6),
        (10, 2, 5),
        (18, 10, 1.8),
        (12, 4, 3)
    ]
)
def test_divide(a, b, expected):
    assert calc.divide(a, b) == expected
    