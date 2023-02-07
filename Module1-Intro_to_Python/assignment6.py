"""
This file contains assignment6 program.

Author: Jonah Hart

Default Command-Line Usage:
    
    pyhon assignment6.py arg1 arg2 arg3 

Modules
-------
sys:
    sys module imported for use of argv object
    
Functions
---------
string.format()
    Used to format a string

print()
    Used to print a formatted string statement
"""

from sys import argv 
script, arg1, arg2, arg3 = argv

print("This script is named {}".format(script))
print("The value of argument 1 is: {}".format(arg1))
print("The value of argument 2 is: {}".format(arg2))
print("The value of argument 3 is: {}".format(arg3))