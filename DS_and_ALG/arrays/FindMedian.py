"""

"""


def merge(a1, a2):
    """
    Merges two sorted array
    :param a1:
    :param a2:
    :return:
    """
    res = []

    i = 0 #iterates through a1
    j = 0 #iterates through a2

    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            res.append(a1[i])
            i+=1
        else:
            res.append(a2[j])
            j+=1

    while i < len(a1):
        res.append(a1[i])
        i+=1

    while j < len(a2):
        res.append(a2[j])
        j+=1

    return res



def mergesort(a):
    """
    Uses divide and conquer approach to solve it
    :param a1:
    :return:
    """

    if not a:
        return

    if len(a) > 1:
        mid = int(len(a)/2)
        a1 = mergesort(a[:mid])
        a2 = mergesort(a[mid:])
        result = merge(a1,a2)
        return result
    else:
        return a


def GetMedian(a1,a2):
    """
    Finds median of two sorted arrays
    :param a1:
    :param a2:
    :return:
    """
    #    Definition of median: if length odd, take middle element, if lenght even, take avg
    # merge two arrays into a sorted array
    # Time complexity O(n) and space complexity of O(n)
    merge = []

    i = 0
    j = 0

    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            merge.append(a1[i])
            i +=1
        else:
            merge.append(a2[j])
            j+=1

    while i < len(a1):
        merge.append(a1[i])
        i+=1

    while j < len(a2):
        merge.append(a2[j])
        j+=1

    print(merge)

    if len(merge) % 2 == 0:
        #even
        middle = int(len(merge)/2)
        median = (merge[middle] + merge[middle-1])/2
    else:
        #odd
        middle = int(len(merge)/2)
        median = merge[middle]

    return median


def GetMedian2(a1, a2):
    """
    Assuming a1 and a2 are same size and sorted
    :param a1:
    :param a2:
    :return:
    """

    #Size of a1 and a2 will be 2n which means overall merged array size is even, median = int((a[n] + a[n-1])/2)

    # count     n=len(a1)
    #0, 1, 2, 3
    #0, 1, 2, 3

    # _ _ _ _ _ _

    i = 0 #index for a1
    j = 0 #index for a2
    c = 0 #count to check if we reached n

    median = 0

    while c < len(a1):
        if i == len(a1) -1:
            median = (a2[j] + a1[i])/2
            break
        elif j == len(a1) -1:
            median = (a2[j] + a1[i])/2
            break

        if c == len(a1) -1:
            median = (a1[i] + a2[j])/2
            break

        if a1[i] < a2[j]:
            i+=1
        else:
            j+=1


        c += 1

    return median

def findMedian(a):
    """
    Finds median of a sorted array
    :param a:
    :return:
    """

    if not a:
        return None

    if len(a) % 2 == 0:
        #Even
        m = int(len(a)/2)
        median = (a[m]+a[m-1])/2
    else:
        #Odd
        m = int(len(a)/2)
        median = a[m]
    return median

def GetMedian3(a1,a2):
    """
    Recursive method O(log n ) approach
    :param a1:
    :param a2:
    :return:
    """

    """
    [1,2,3,4,5,6] 6/2=3 a[:mid+1]
    3.5
    [0,0,0,0,10,10] a[mid-1:]
    0
    
    [1,2,3,4]
    2.5
    [0,0,10,10]
    5
    
    [2,3,4]
    3
    [0,0,10]
    0
    
    [2,3]
    [0,10]
    """


    #Base case
    if len(a1) == 2 and len(a2) == 2:
        #Call merge function to merge
        result = merge(a1,a2)
        median = (result[1] +result[2])/2
        return median
    elif len(a1) != len(a2):
        return "Not Applicable"
    elif len(a1) ==0 or len(a2)==0:
        return "Nothing array"
    elif len(a1) == 1:
        return (a1[0] + a2[1]) / 2

    else:
        m1 = findMedian(a1)
        m2 = findMedian(a2)

        n = len(a1)

        if m1 > m2:

            if n % 2 == 0:
                return GetMedian3(a1[:int(n / 2) + 1],
                                 a2[int(n / 2) - 1:])
            else:
                return GetMedian3(a1[:int(n / 2) + 1],
                                 a2[int(n / 2):])

        else:
            if n % 2 == 0:
                return GetMedian3(a1[int(n / 2 - 1):],
                                 a2[:int(n / 2 + 1)])
            else:
                return GetMedian3(a1[int(n / 2):],
                                 a2[0:int(n / 2) + 1])


if __name__ == '__main__':
    a1=[1,2,3]
    a2=[6,8,1,0,2,34,21]
    a3 = [6,8,9]

    a1 = [1, 12, 15, 26, 38]
    a3 = [2, 13, 17, 30, 45]
    # 0,1,2,3,6,8 --> 3+2/2 == 5/2 = 2.5

    #print(GetMedian(a1,a3))
    #print(GetMedian2(a1,a3))
    print(GetMedian3(a1,a3))
   #print(mergesort(a2))
