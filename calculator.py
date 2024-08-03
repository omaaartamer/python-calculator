import sys

"""
This module is a basic calculator that performs basic operations on 2 numbers.
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
    """Return the difference of c and d."""
    return c - d

def multiply(e, f):
    """
    Multiply two numbers and return the result.

    Parameters:
    e (float): The first number.
    f (float): The second number.

    Returns:
    float: The product of e and f.
    """
    return e * f

def divide(g, h):
    """Return the division of g by h. Raise ValueError if h is zero."""
    if h == 0:
        raise ValueError("Cannot divide by zero")
    return g / h

def modulus(i, j):
    """Return the modulus of i by j."""
    return i % j

def main(x,y, oper):
    # Ensure that the correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python calculator.py <number1> <number2> <operation>")
        print("Operations: add, subtract, multiply, divide, modulus")
        sys.exit(1)

    # Parse command-line arguments
    try:
        a = float(x)
        b = float(y)
    except ValueError as e:
        print(f"Error: Invalid number. {e}")
        sys.exit(1)

    operation = oper.lower()

    # Define available operations
    operations = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide,
        'modulus': modulus
    }

    # Get the function based on the operation argument
    func = operations.get(operation)

    # Perform the calculation and handle errors
    if func:
        try:
            result = func(a, b)
            print(f"Result: {result:.2f}")
        except ValueError as e:
            print(f"Error: {e}")
    else:
        print("Unsupported Operation. Supported operations: add, subtract, multiply, divide, modulus.")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2],sys.argv[3])
