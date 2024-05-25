import pytest
from calculator import Calculator, CalculatorOptions


def test_sum():
    calc = Calculator()
    assert calc.calc(CalculatorOptions.SUM.value, 1, 2) == 3
    assert calc.calc(CalculatorOptions.SUM.value, -1, -1) == -2
    assert calc.calc(CalculatorOptions.SUM.value, 1.5, 2.5) == 4.0


def test_subtraction():
    calc = Calculator()
    assert calc.calc(CalculatorOptions.SUBTRACTION.value, 3, 2) == 1
    assert calc.calc(CalculatorOptions.SUBTRACTION.value, 1, -1) == 2
    assert calc.calc(CalculatorOptions.SUBTRACTION.value, 1.5, 0.5) == 1.0


def test_times():
    calc = Calculator()
    assert calc.calc(CalculatorOptions.TIMES.value, 3, 2) == 6
    assert calc.calc(CalculatorOptions.TIMES.value, -1, -1) == 1
    assert calc.calc(CalculatorOptions.TIMES.value, 1.5, 2) == 3.0


def test_division():
    calc = Calculator()
    assert calc.calc(CalculatorOptions.DIVISION.value, 6, 2) == 3
    assert calc.calc(CalculatorOptions.DIVISION.value, -4, -2) == 2
    assert calc.calc(CalculatorOptions.DIVISION.value, 1.5, 0.5) == 3.0

    with pytest.raises(ValueError, match="Division by zero is not allowed"):
        calc.calc(CalculatorOptions.DIVISION.value, 1, 0)


def test_pow():
    calc = Calculator()
    assert calc.calc(CalculatorOptions.POW.value, 2, 3) == 8
    assert calc.calc(CalculatorOptions.POW.value, 4, 0.5) == 2.0
    assert calc.calc(CalculatorOptions.POW.value, 2, -1) == 0.5


def test_unsupported_operation():
    calc = Calculator()
    with pytest.raises(ValueError, match="Unsupported operation"):
        calc.calc(999, 1, 1)

