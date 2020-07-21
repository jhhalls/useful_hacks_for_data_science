#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 23:02:34 2020

@author: jhhalls
"""

#The strings are immutable in python
# i.e. you cannot reassign the elements

# lets check it out

x = "github"
print (type(x))


# lets try to reassign the elements
#x[0] = "G"

# We can further verify this by checking the memory location 
# address of the position of the letters of the string.

for i in range(0,6):
    print (x[i], "=" , id(x[i]))