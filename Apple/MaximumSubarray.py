"""
Given an integer array nums,
find the contiguous subarray within an array
(containing at least one number) which has the largest product or sum.

Bottleneck
Unnecessary
and Duplicate work


https://www.youtube.com/watch?v=2MmGzdiKR9Y&t=301s

https://www.youtube.com/watch?v=86CQq3pKSUw
"""
import sys




def findProd(a):
    prod = 1
    if not a:
        return 0
    else:
        for e in a:
            prod = prod*e

    return prod



def findSum(a):
    return sum(a)


def maxSubProd(a):
    fs = 0
    sa = []

    for i in range(len(a)):
        for j in range(i, len(a)):
            print(a[i:j + 1])
            cs = findProd(a[i:j + 1])
            if cs > fs:
                fs = cs
                sa = a[i:j + 1]

    return (fs, sa)

def maxSubSum(a):
    """
    O(n^3)
    :param a:
    :return:
    """
    fs = 0
    sa = []

    for i in range(len(a)):
        for j in range(i,len(a)):
            print(a[i:j+1])


            cs = findSum(a[i:j+1])
            if cs > fs:
                fs = cs
                sa = a[i:j+1]

    return (fs,sa)

def maxSubSum2(a):
    """
    Quadratic method
    :param a:
    :return:
    """
    fa = 0

    for i in range(len(a)):
        win = 0
        for j in range(len(a)):
            print(i,j)
            win += a[j]
            print(win)
            print("---------")
            if win > fa:
                fa = win

    return fa

def maxSubSum3(a):
    """
    O(n) solution dynamic programming
    [0,45,-1,65]
    [0 = 0, 45, 45, 65+45]
    :param a:
    :return:
    """
    if not a:
        return

    st = []
    pb = float("-inf")

    for i in range(len(a)):
        #first element check
        if not st:
            st.append(a[i])
        else:
            s = st[-1]+a[i]
            if s>a[i]:
                st.append(s)
            else:
                st.append(a[i])

    print(st)

    highest = max(st)
    i = st.index(highest)
    ms = a[:i+1]

    print(ms)


    return highest





if __name__ == "__main__":
    a = [1,3,4]
    a=[0,0,3]
    a = [0,45,-1,65,-2,-90,-47]
    a= [0,0,14,56,6]
    a= [1,-3,2,1,-1]
    a=[-2,3,2,-1,-1,-98]


    print(maxSubSum3(a))

