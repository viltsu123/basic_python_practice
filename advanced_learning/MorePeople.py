'''
This is a script for generating more people.
So i chose exercise three of the provided material.
The main logic is here for creating people.
'''

import sys
from Person import Person

argument = int(input("please give an integer of how many people to great!"))

try:
    #check input is there and cast as int
    if len(sys.argv) == 0:
        argument = input("please give inout as integer: ")
except:
    print("virhe, lopetetaan")
else:
    print("")


if isinstance(argument, int):
    if argument < 2:
        print("Starting machine, creating {} person...".format(str(argument)))
    else:
        print("Starting machine, creating {} peoples...".format(str(argument)))
else:
    print("that was not an integer, shutting down...")

peoples = []

for i in range(0,argument):
    p = Person()
    peoples.append(p)

for i in range(0, len(peoples)):
    print(peoples[i])
