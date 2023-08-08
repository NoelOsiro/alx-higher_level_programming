#!/usr/bin/python3

"""Print the alphabet in lowercase, not followed by a new line."""
alphabet = ""
for i in range(97, 123):
    alphabet += chr(i)

print("{}".format(alphabet), end="")
