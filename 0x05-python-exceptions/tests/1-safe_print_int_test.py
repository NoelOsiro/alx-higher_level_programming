#!/usr/bin/python3
def safe_print_integer(value):
    try:
        formatted_value = "{:d}".format(value)
        print(formatted_value)
        return True
    except:
        return False

def test_safe_print_integer():
    # Test case 1: Printing a valid integer
    result = safe_print_integer(123)
    assert result is True

    # Test case 2: Printing a string
    result = safe_print_integer("abc")
    assert result is False

    # Test case 3: Printing a float
    result = safe_print_integer(3.14)
    assert result is False

    # Test case 4: Printing a negative integer
    result = safe_print_integer(-456)
    assert result is True

    # Test case 5: Printing a boolean
    result = safe_print_integer(True)
    assert result is True

    print("All test cases passed!")

# Run the tests
test_safe_print_integer()
