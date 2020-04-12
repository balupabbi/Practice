"""
Example Python Syntax (will also be provided during the
interview)
Loops
for x in l: 'Iterate on x for each value in list'
for i in range(0,5): 'Iterate on i from value 0 to 4'
for k, v in d.items(): 'Iterate on each key, value pair in dict'
Lists (Array)
l = [] 'Define an empty list'
l[i] 'Return value at index i in list'
len(l) 'Return length of list'
l.append(x) 'Add value x to the end of list'
l.sort() 'Sort values in list - in place sort, returns None'
sorted(l) 'Return sorted copy of list'
x in l: 'Evaluate True if x is contained in the list'
Dictionary (HashMap)
d = {} 'Define an empty Dictionary'
d[x] 'Return value for key x'
d[x] = 1 'Set value for key x to 1'
d.keys() 'Return list of keys'
d.values() 'Return list of values'
Tuple
tup = ()
tup = (1,2) + tup
Other functions
reversed(n) 'reverse a list'
random.random() 'random number between 0 and 1'
random.randrange(start, stop) 'Return a randomly selected element
from range(start, stop)'
isinstance(x, list) 'returns True if x is instance of list'
split() 'returns a list of all the words in the string'
ceil() 'returns the smallest integer value greater than or equal
to x

"""


import math

def oddPosition(a):
    """
    Write a function that returns the elements on odd positions (0 based) in a list

    """
    # 0,1,2,3,4 --> 1,2,3
    res = []
    for i in range(1,len(a),2):
        res.append(a[i])

    print(res)
    return res

def oddPosition2(a):
    """
     Write a function that returns the elements on odd positions (0 based) in a list INPLACE
    :param a:
    :return:
     """
    return a[1::2]

def Sum(a):
    """
    Write a function that returns the cumulative sum of elements in a list

    :param a:
    :return:
    """
    cs = 0
    res = []

    for i in range(len(a)):
        cs += a[i]
        res.append(cs)

    #Use list comprehension
    res = [sum(a[0:i+1]) for i in range(len(a))]
    return res


if __name__ == "__main__":
    a = [0,1,2,3,4,5,6,7]
    # res = oddPosition2(a)
    # assert oddPosition2([0, 1, 2, 3, 4, 5]) == [1, 3, 5]
    # assert oddPosition2([1, -1, 2, -2]) == [-1, -2]
    print(Sum(a))
    assert Sum([1, 1, 1]) == [1, 2, 3]
    assert Sum([1, -1, 3]) == [1, 0, 3]



