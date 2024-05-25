import os, sys

from calculator import CalculatorOptions, Calculator


if __name__ == "__main__":
    print("\nBasic Python Calculator!")

    choice = 0
    print("\nSelect your option:")

    for option in CalculatorOptions:
        print(f"{option.value} - {option.name}")

    while choice not in [i.value for i in CalculatorOptions]:
        try:
            choice = int(input("\nDigit your option: "))
        except ValueError:
            print("You need to digit a number!")

    num1, num2 = float(input("First Number: ")), float(input("Second Number: "))

    instance = Calculator()
    print(f"Result is {instance.calc(choice=choice, num1=num1, num2=num2)}")

