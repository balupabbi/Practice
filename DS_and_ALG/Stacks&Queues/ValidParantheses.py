
"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
"""
from collections import defaultdict


def validParantheses(s):
    """

    :return:
    """
    brac = {')':'(', ']':'[', '}':'{'}
    open = ['(','[','{']
    closed = [')',']','}']

    st = defaultdict(int) #keys will be open
    stack = []

    #'()[]{}'

    for i in s:
        if i in open:
            stack.append(i)
        elif i in closed:
            if stack:
                cp = stack.pop()
                if brac[i] != cp:
                    return False

    if len(stack) == 0:
        return True
    else:
        return False








if __name__ == "__main__":
    ex = '()[]{}'
    ex = '([)]'
    ex = '(]'
    ex = '{[]}'
    if validParantheses(ex):
        print("Valid")
    else:
        print("Invalid")
