#!/usr/bin/python3
if __name__ == "__main__":
    """Print the sum, difference, multiple and quotient of 10 and 5."""
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5
    format_string = "{} {} {} = {}"

    print(format_string.format(a, "+", b, add(a, b)))
    print(format_string.format(a, "-", b, sub(a, b)))
    print(format_string.format(a, "*", b, mul(a, b)))
    print(format_string.format(a, "/", b, div(a, b)))
