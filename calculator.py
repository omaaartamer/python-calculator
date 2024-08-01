"""
    This module is a basic calculator the does basic operations on 2 integers.
"""


def add(a, b):
    """
    Add two numbers and return the result.

    Parameters:
    a (float): The first number.
    b (float): The second number.

    Returns:
    float: The sum of the numbers.
    """
    return a + b


def subtract(c, d):
    """Return the difference of a and b."""
    return c-d


def multiply(e, f):
    """
    Multiply two numbers and return the result.

    Parameters:
    a (float): The first number.
    b (float): The second number.

    Returns:
    float: The product of a and b.
    """
    return e*f


def divide(g, h):
    """Return the division of a by b. Raise ValueError if b is zero."""
    if h == 0:
        raise ValueError("Cannot divide by zero")
    return g/h


def modulus(i, j):
    """Return the modulus of a by b."""
    return i % j


if __name__ == "__main__":
    operation = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide,
        'modulus': modulus
    }
    ENTRY = True
    while ENTRY:
        try:
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            ENTRY = False
        except ValueError as e:
            print(f"Error: {e}")

    action = input(
        "(add, subtract, divide, multiply, modulus): ").strip().lower()
    func = operation.get(action)
    if func:
        try:
            result = func(x, y)
            print(f"{result:.2f}")
        except ValueError as e:
            print(f"Error {e}")
    else:
        print("Unsupported Operation.")
