"""
Python Questions -
1) Print Max element of a given list
2) Print median of a given list
3) Print the first nonrecurring element in a list
4) Print the most recurring element in a list
5) Greatest common Factor



"""





def stringinfo():
    """
    Use fstring for interviews
    :return:
    """
    marks = 100
    tes = f'i just got {marks} marks on my test. I am sooo happy'
    print(tes)



def listComprehension():
    numbers = [0,1,2,3,4]

    def square(x):
        return x*x

    resm = map(square, numbers)
    res = [square(x) for x in numbers] #advised to use list comprehension in interviews

    def is_odd(x):
        return bool(x % 2)

    resf = filter(is_odd,numbers)
    reslf = [x for x in numbers if is_odd(x)]


def Iteration(a):

    #index and element
    for i, e in reversed(list(enumerate(a))):
        print(i, e)

    # 2 .. len(a)-1
    for i, num in enumerate(a, start=2):
        print(i, num)

    #just element
    for e in reversed(a):
        print(e)

    """
    range(stop) takes one argument.
    range(start, stop) takes two arguments.
    range(start, stop, step) takes three arguments.
    """

    # print 1,...7
    for i in range(1, 8):
        print(i)

    #prints 3,6,9,12,15, skips by 3, Incrementing
    for i in range(3,16,3):
        print(i)

    #Decrementing using range, prints 10,8,6,4,2,0,-2,-4
    for i in range(10, -6, -2):
        print(i)

    #Just basic reverse using range, prints 4,3,2,1,0
    for i in reversed(range(5)):
        print (i)


def FizzBuzz(a):
    """
    1) Replace all integers that are evenly divisible by 3 with "fizz"
    2) Replace all integers divisible by 5 with "buzz"
    3) Replace all integers divisible by both 3 and 5 with "fizzbuzz"
    :return:
    """

    for i, v in enumerate(a):
        if v % 3 == 0:
            a[i] = "fizz"
        elif v % 5 == 0:
            a[i] = "buzz"
        elif v % 5 == 0 and v % 3 == 0:
            a[i] = "fizzbuzz"

    print(a)







if __name__ == "__main__":
    a = [0,10,12,13,45]

    #FizzBuzz(a)
    stringinfo()

