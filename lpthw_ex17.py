# Learning Python3 the Hard Way - Exercise 17. More Files.

from sys import argv; from os.path import exists; from datetime import datetime; script, from_file, to_file = argv; indata = open(from_file).read(); open(to_file, 'w').write(indata)

with open(script) as f:
    print(f"This script has {len(f.readlines())} number of lines.")

print(f"The current time is {datetime.now().time()}.")
