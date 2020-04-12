







def intersect2(a,a1):
    """

    :param a:
    :param a1:
    :return:
    """
    output = set()

    a = set(a)
    a1 = set(a1)

    if len(a)> len(a1):
        output = a.intersection(a1)
        output = list(output)
    else:
        output = a1.intersection(a)
        output = list(output)

    print(output)


def intersect(a,a1):
    """
    Brute Fore
    :param a:
    :param a1:
    :return:
    """

    intersected = []

    for i, v in enumerate(a):
        for j, v2 in enumerate(a1):
            if v == v2:
                if v not in intersected:
                    intersected.append(v)

    print(intersected)






if __name__ == '__main__':
    a = [34,56,1,2,3]
    a1 = [1,2]
    intersect2(a,a1)