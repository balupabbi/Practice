





"""
[[1,5],[3,7],[4,6],[6,8],[10,12],[12,15]]

[1,5] [4,6]  [3,7] [6,8] [10,12] [12,15]

"""


def mergeOverlap(a):
    """
    O(log n)
    :param a:
    :return:
    """
    if not a:
        return

    res = []

    if not a:
        return None

    a.sort(key = lambda x: x[1])

    s = a[0][0]


    for i in range(len(a)-1):

        ce = a[i][1]

        if ce < a[i+1][0]:
            res.append([s,ce])
            s = a[i+1][0]

    if res:
        res.append([s,a[len(a)-1][1]])



    return res







if __name__ == '__main__':
    a = [[1,5],[3,7],[4,6],[6,8],[10,12],[16,20],[18,20],[12,15]]
    #a = []

    out = mergeOverlap(a)
    print(out)