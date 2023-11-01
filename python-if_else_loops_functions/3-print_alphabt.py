#!/usr/bin/python3
for i in range(ord('a'), ord('z')+1):
    picker = chr(i)
    if picker== 'q' or picker== 'e':
        continue
    print("{:s}".format(picker), end="")
