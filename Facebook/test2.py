#Given k numbers which are less than n, return the set of prime numbers among them

#Friends problem [[A,B], [B,D],[E]...] ( List of lists);


from collections import defaultdict




def mostfriends(n):

    d = defaultdict(int)

    for e in n:
        if len(e) > 1:
            d[e[0]] += 1

    f = None
    mf = 0

    for k,v in d.items():
        if v > mf:
            mf = v
            f = k

    return f





def getprime(n,k):

    """
    Prime is any number greater than 1 where this number is only divisible by itself and nothing else
    :param n:
    :param k:
    :return:
    """
    def checkPrime(n):

        for i in range(2,(n-1)):
            if n%i == 0:
                return False

        return True

    res = []

    for digit in range(2,n+1):
        if checkPrime(digit):
            if len(res) < k:
                res.append(digit)
            elif len(res) == k:
                break

    return res







if __name__ == "__main__":
    n= 12
    k= 5
    #print(getprime(n,k))

    friends = [['A','B'],['A', 'C'],['B','C'],['C','D']]
    print(mostfriends(friends))