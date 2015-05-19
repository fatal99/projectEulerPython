#!/usr/bin/python
# -*- coding: utf-8 -*-

# ========================================================================== #
#                                      									     #
#                 									                         #
#      				   Project Euler : probleme ___        			 	     #
#                                           						         #
#                                           						    	 #
# ========================================================================== #

# Triangle, pentagonal, and hexagonal numbers are generated by the following 
# formulae:
# 
# Triangle        Tn=n(n+1)/2     1, 3, 6, 10, 15, ...
# Pentagonal      Pn=n(3n−1)/2        1, 5, 12, 22, 35, ...
# Hexagonal       Hn=n(2n−1)      1, 6, 15, 28, 45, ...
# It can be verified that T285 = P165 = H143 = 40755.
# 
# Find the next triangle number that is also pentagonal and hexagonal.

import time
import math

def is_pentagonal(n):
    """
    int -> bool : check if an integer is pentagonal number by ealuating the 
    inverse function
    """
    inverse = (1 + math.sqrt(1 + 24*n))/6
    return inverse.is_integer()

def is_hexagonal(n):
    """
    int -> bool : check if an integer is hexagonal number by ealuating the 
    inverse function
    """
    inverse = (1 + math.sqrt(1 + 8*n))/4
    return inverse.is_integer()

def euler_45():
    """
    unit -> bool : return the solution of problem 45
    """
    res = False  # True when we find the solution
    cur_pos = 286  # we start from 286 to find the next one
    while not(res):
        n = cur_pos*(cur_pos + 1)/2 
        if is_hexagonal(n) and is_pentagonal(n):
            return n
        else:
            cur_pos += 1


def main():
    # print is_hexagonal(40755)
    # print is_pentagonal(40755)
    # print is_pentagonal(4075)
    t = time.time()
    print euler_45()
    print time.time() - t

# =========================== #
#                             #
#           Tests             #
#                             #
# =========================== #

if __name__ == '__main__':
    main()
