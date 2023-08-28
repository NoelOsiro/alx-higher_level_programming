#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        printed_count = 0
        for element in my_list:
            if printed_count < x:
                print(element,end='')
                printed_count += 1
            else:
                break
        print()
        return printed_count
    except:
        return printed_count
