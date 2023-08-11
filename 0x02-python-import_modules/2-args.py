#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv[1:]  # Exclude the script name itself
    num_args = len(argv)

    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print(f"1 argument:\n1: {argv[0]}")
    else:
        print(f"{num_args} arguments:")
        for i, arg in enumerate(argv, start=1):
            print(f"{i}: {arg}")
