from src.main import Calc
import pytest
from contextlib import nullcontext as does_not_raise


class TestCalculator:
    @pytest.mark.parametrize(
        "num1, num2, res",
        [(1, 2, 2), (0.1, 0.1, 0.010000000000000002), (5, 2, 10), (5, -1, -5)],
    )
    def test_multiply(self, num1, num2, res):
        assert Calc.mult(num1, num2) == res

    @pytest.mark.parametrize(
        "num1, num2, res, expected",
        [(6, 2, 3, does_not_raise()),
         (3, 3, 1, does_not_raise()),
         (5, 0, -5, pytest.raises(ZeroDivisionError))],
    )
    def test_divide(self, num1, num2, res, expected):
        with expected:
            assert Calc.div(num1, num2) == res
