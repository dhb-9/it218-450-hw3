from decimal import Decimal
from typing import Callable
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract, multiply, divide

class Calculator:
    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        calculation = Calculation(a, b, operation)
        Calculations.add_calculation(calculation)
        return calculation.perform()

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        calculation = Calculation(a, b, add)
        return calculation.get_result
    
    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        calculation = Calculation(a, b, subtract)
        return calculation.get_result
    
    @staticmethod
    def mutliply(a: Decimal, b: Decimal) -> Decimal:
        calculation = Calculation(a, b, multiply)
        return calculation.get_result
    
    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        calculation = Calculation(a, b, divide)
        return calculation.get_result
