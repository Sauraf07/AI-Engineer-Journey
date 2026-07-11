"""Reusable calculator operations."""


def calculate(first: float, second: float, operation: str) -> float:
    """Calculate *first operation second* and return the answer."""
    operations = {
        "+": lambda: first + second,
        "-": lambda: first - second,
        "*": lambda: first * second,
        "/": lambda: first / second,
    }
    if operation not in operations:
        raise ValueError("Choose one of: +, -, *, /.")
    if operation == "/" and second == 0:
        raise ValueError("Division by zero is not allowed.")
    return operations[operation]()


def calculate_from_input() -> float:
    """Read a calculation from the terminal."""
    try:
        first = float(input("Enter first number: "))
        second = float(input("Enter second number: "))
    except ValueError as error:
        raise ValueError("Please enter valid numbers.") from error
    operation = input("Choose operation: ").strip()
    return calculate(first, second, operation)
