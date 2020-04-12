

def convertint(n):

    res = []

    for i in str(n):
        res.append(int(i))

    return res




if __name__ == "__main__":
    a = [[0,2,3],[34,56,7],[8,6,5]]

    b = [1,2,3,4,5]

    n = 128

    print(convertint(n))



    # for i in range(1,len(b),2):
    #     print (b[i])
    #
    #
    # for i in range(len(b)):
    #
    #     if i%2==1:
    #         print(b[i])

    # res = 1
    #
    # for i in b:
    #     res = res* i
    # print(res)


