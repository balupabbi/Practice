#!/bin/python3

import math
import os
import random
import re
import sys



def rotateright_fast(nums,k):
    """
    do it in place
    :param a:
    :param r:
    :return:
    """
    n = len(nums)
    k %= n

    start = count = 0
    while count < n:
        current, prev = start, nums[start]
        while True:
            next_idx = (current + k) % n
            nums[next_idx], prev = prev, nums[next_idx]
            current = next_idx
            count += 1

            if start == current:
                break
        start += 1


def rotateright_BF(nums,k):
    """
    Time Complexity O(n*k), Space Complexity O(1)
    :param a:
    :param r:
    :return:
    """

    # for i in range(k):
    #     previous = nums[-1]
    #     for j in range(len(nums)):
    #         nums[j], previous = previous, nums[j]

    for i in range(k):
        previous = nums[-1]
        for j in range(len(nums)):
            tmp = nums[j]
            nums[j] = previous
            previous = tmp

    return nums







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
    a =[1, 2, 3, 4, 5, 6, 7]
    k = 3
    print(rotateright_BF(a,k))
   #print (rotateright(a,k))

   #print(rotLeft(a,1))
   #print(rotateright(a,1))