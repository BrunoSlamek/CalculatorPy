from enum import Enum
from typing import Union, Callable

Number = Union[int, float]
DEFAULT_RETURN, DEFAULT_TYPES = Number, Number


class CalculatorOptions(Enum):
    SUM = 1
    SUBTRACTION = 2
    TIMES = 3
    DIVISION = 4
    POW = 5


class Calculator:

    def __init__(self) -> None:
        self.operations = {
            CalculatorOptions.SUM: self._sum,
            CalculatorOptions.SUBTRACTION: self._sub,
            CalculatorOptions.TIMES: self._times,
            CalculatorOptions.DIVISION: self._div,
            CalculatorOptions.POW: self._pow
        }

    @staticmethod
    def _sum(a: DEFAULT_TYPES, b: DEFAULT_TYPES) -> DEFAULT_RETURN: return a + b

    @staticmethod
    def _sub(a: DEFAULT_TYPES, b: DEFAULT_TYPES) -> DEFAULT_RETURN: return a - b

    @staticmethod
    def _times(a: DEFAULT_TYPES, b: DEFAULT_TYPES) -> DEFAULT_RETURN: return a * b

    @staticmethod
    def _div(a: DEFAULT_TYPES, b: DEFAULT_TYPES) -> DEFAULT_RETURN: 
        if b == 0: 
            raise ValueError("Division by zero is not allowed")
        return a / b

    @staticmethod
    def _pow(a: DEFAULT_TYPES, b: DEFAULT_TYPES) -> DEFAULT_RETURN: return a ** b

    def calc(self, choice: int, num1: Number, num2: Number) -> Number:
        try:
            operation: Callable[[Number, Number], Number] = self.operations[CalculatorOptions(choice)]
        except KeyError:
            raise ValueError(f"Unsupported operation: {choice}")
        return operation(num1, num2)
