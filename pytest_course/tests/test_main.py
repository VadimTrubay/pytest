from src.main import Calc
import pytest


@pytest.mark.parametrize(
    "num1, num2, res",
    [(1, 2, 2), (0.1, 0.1, 0.010000000000000002), (5, 2, 10), (5, -1, -5)],
)
def test_multiply(num1, num2, res):
    assert Calc.mult(num1, num2) == res


@pytest.mark.parametrize(
    "num1, num2, res",
    [(6, 2, 3), (3, 3, 1), (5, -1, -5)],
)
def test_divide(num1, num2, res):
    assert Calc.div(num1, num2) == res
    with pytest.raises(ZeroDivisionError):
        Calc.div(num1, 0)
