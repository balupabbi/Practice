
"""
Given an array of integers and a value, determine if there are any three integers in the array whose sum equals the given value.
"""




"""
23,5,3,1

23,5,3
23,5,1

23,3,1

5,3,1

3,1,

"""

def BruteForcethreeSome(a,t):
    """
    O(n^3)
    :param a:
    :param t:
    :return:
    """
    res = []

    for i in range(len(a)):
        for j in range(i+1, len(a)):
            for k in range(j+1,len(a)):
                cl = [a[i],a[j],a[k]]
                print(sum(cl))
                if sum(cl) == t:
                    res.append(cl)


    return res


"""
23,5,3,1


23:1, 5:2, 3:3, 1:4

1,3,5,6,23 --sorted

1,

"""
def SortingthreeSome(a,t):
    """

    :param a:
    :param t:
    :return:
    """
    a.sort()
    ht = {}
    ans = []

    for i,v in enumerate(a):
        ht[v] = i

    for i in range(len(a)):
        for j in range(i+1,len(a)):
            cs = a[i]+a[j]
            tv = t-(cs)

            if tv in ht and ht[tv]>j:
                cl = [a[i],a[j],tv]
                ans.append(cl)

    return ans









if __name__ == '__main__':
    a = [23,5,6,3,1]
    t = 29

    #res = BruteForcethreeSome(a,t)
    res = SortingthreeSome(a,t)
    print(res)