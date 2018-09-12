"""
Determine if string has all unique characters
"""




def unique(samp):
    tes = []
    for i in samp:
        tes.append(i)

    before = len(tes)
    tes.sort()
    after = len(tes)

    if (before == after):
        return True
    else:
        return False
    #Sort tes and check to see if sorted list and tes have same lenght, if yes then unique other its false
    #print (tes)


if __name__ == "__main__":
    res = unique("ddd")

    print(res)
