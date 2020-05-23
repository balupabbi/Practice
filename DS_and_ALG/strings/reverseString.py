










def reverse(c):
    """
    two pointers method
    :param c:
    :return:
    """

    if not c:
        return c
    
    i = 0
    j = len(c)-1

    while i < j:
        tmp = c[i]
        c[i] = c[j]
        c[j] = tmp

        i += 1
        j -= 1


    return c






if __name__ == "__main__":
    c = ["h", "e", "l", "l", "o"]
    c = ["H","a","n","n","a","h"]

    print(reverse(c))