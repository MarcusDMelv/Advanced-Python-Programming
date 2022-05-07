from functions import *  # todo import functions module

import code  # todo import code package


# function from function.py
hello()

capital_a = code.A()  # from code package __init__.py
capital_b = code.B()
capital_a
capital_b

"""
Relative imports - 
    based on location import this 
"""
import code.a

"""
import run.py from package main
"""
import main.a.p1.run

"""
import something.py from main package
"""
import  main.b.p2.something

