#!/usr/bin/python3

"""Print numbers 0 to 98 in decimal and hexadecimal."""
for i in range(99):
    print("{} = 0x{:02x}".format(i, i))
