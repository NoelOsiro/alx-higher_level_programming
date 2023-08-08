#!/usr/bin/python3

for i in range(122, 96, -1):
    char = chr(i).lower() if i % 2 == 0 else chr(i).upper()
    print("{}".format(char), end="")
