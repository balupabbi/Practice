#!/bin/python3

import math
import os
import random
import re
import sys




def rotateright(a,d):
    #Extra space
    b = [i for i in range(len(a))]


    for i in range(len(a)):
        b_index = (i+d) % len(a) #it will only go from 0 to 4

        b[b_index] = a[i]



    return b

# Complete the rotLeft function below.
def rotLeft(a, d):
    b = [i for i in range(len(a))]

    for i in range(len(a)):
        a_index = (i+d) % len(a) # it will only go from 0 to 4

        b[i] = a[a_index]

    return b


if __name__ == '__main__':
   a=[1,2,3,4,5]
   print(rotLeft(a,1))
   print(rotateright(a,1))