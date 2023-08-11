#!/usr/bin/python3

import sys

if __name__ == "__main__":
    argv = sys.argv[1:]  # Exclude the script name itself
    total = sum(int(arg) for arg in argv)
    print(f"{total}")
