#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        printed_count = 0
        for element in my_list:
            if printed_count < x:
                print(element, end=" ")
                printed_count += 1
            else:
                break
        print()
        return printed_count
    except:
        return printed_count

def test_safe_print_list():
    # Test case 1: Print 3 elements from a list of 5
    my_list = [1, 2, 3, 4, 5]
    num_printed = safe_print_list(my_list, 3)
    assert num_printed == 3

    # Test case 2: Print 7 elements from a list of 5
    num_printed = safe_print_list(my_list, 7)
    assert num_printed == 5

    # Test case 3: Print 0 elements from a list of 5
    num_printed = safe_print_list(my_list, 0)
    assert num_printed == 0

    # Test case 4: Print 3 elements from an empty list
    empty_list = []
    num_printed = safe_print_list(empty_list, 3)
    assert num_printed == 0

    # Test case 5: Print 3 elements from a list of strings
    string_list = ["apple", "banana", "cherry", "date"]
    num_printed = safe_print_list(string_list, 3)
    assert num_printed == 3

    print("All test cases passed!")

# Run the tests
test_safe_print_list()
