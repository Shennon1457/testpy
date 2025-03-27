from src.calc import Calculator as bas

calc = bas()

def test_sum():
    assert calc.sum(1, 2) == 3
    assert calc.sum(4, 5) == 9
    assert calc.sum(3, -3) == 0
    assert calc.sum(3, 3) == 6
    assert calc.sum(-3.5, 3) == -0.5

def test_sub():
    assert calc.subtract(8, 2) == 6
    assert calc.subtract(5, 2) == 3
    assert calc.subtract(9, 4) == 5
    assert calc.subtract(8, -4) == 12
    assert calc.subtract(15.5, 10) == 5.5

def test_mult():
    assert calc.multiply(6, 5) == 30
    assert calc.multiply(5, -5) == -25
    assert calc.multiply(10, 2) == 20
    assert calc.multiply(6, 2) == 12
    assert calc.multiply(5, 2) == 10

def test_divide():
    assert calc.divide(20, 10) == 2
    assert calc.divide(81, 9) == 9
    assert calc.divide(36, 6) == 6
    assert calc.divide(55, 5) == 11
    assert calc.divide(60, 6) == 10
