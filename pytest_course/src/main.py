from typing import Union


class Calc:
    @staticmethod
    def mult(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
        return num1 * num2

    @staticmethod
    def div(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
        return num1 / num2
