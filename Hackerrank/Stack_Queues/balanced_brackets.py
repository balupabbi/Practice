
"""
Review of stacks and queue
samp = []

1,2,3 -> 1,2,3
FIFO = queue, use popleft with list and append to add

1,2,3 -> 3,2,1
LIFO = stack, use pop with list and append to add
"""

def geeksisBalanced(s):
    # Python3 code to Check for
    # balanced parentheses in an expression
    open_list = ["[", "{", "("]
    close_list = ["]", "}", ")"]


    stack = []
    for i in s:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                    (open_list[pos] == stack[len(stack) - 1])):
                stack.pop()
            else:
                return "NO"
    if len(stack) == 0:
        return "YES"


def isBalanced(s):

    if not s:
        return

    #keys are closed and open are values
    brackets = {')':'(', '}':'{', ']':'['}

    open = ['(', '{', '[']
    closed = [')','}',']']

    store = []

    for brac in s:
        if brac in open:
            store.append(brac)
        elif brac in closed:
            pos = closed.index(brac)
            if ((len(store) > 0) and
                    (open[pos] == store[len(store) - 1])):
                store.pop()
            else:
                return "NO"
    if store:
        return 'NO'
    else:
        return 'YES'





if __name__ == '__main__':
    tests = ['{{)[](}}','{[()]}', '{[(])}', '{{[[(())]]}}']

    for test in tests:
        print(isBalanced(test))
        #print(geeksisBalanced(test))