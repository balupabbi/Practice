
def merge(res1,res2):

    result = []

    if not res1 and not res2:
        return

    i = 0
    j = 0

    #i index in res1
    #j index in res2

    while ( i <= (len(res1)-1) or j <= (len(res2)-1) ):
        if res1[i] < res2[j]:
            result.append(res1[i])
            i += 1
        elif res2[j] < res2[i]:
            result.append(res2[i])
            j += 1

    while(i <= (len(res1)-1)):
        result.append(res1[i])

    while(j <= (len(res2)-1)):
        result.append(res2[i])

    return result


def merge_sort(a):

    if len(a) > 1:
        middle = len(a)//2

        left = a[:middle]
        right = a[middle:]
        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                a[k]=left[i]
                i += 1
                k += 1
            elif right[j] < left[i]:
                a[k]=right[j]
                j += 1
                k += 1

        while (i < len(left)):
            a[k]=left[i]
            i+=1
            k+=1

        while (j < len(right)):
            a[k]=right[j]
            j+=1
            k+=1



def binary_seach(a, value):

    if not a:
        return False

    a.sort()


    length = len(a)
    middle_index = int(length/2)

    #value is more that max value in the array so return False since it is not in the array or value is less that first element so return False
    if value > a[length-1]:
        return False
    elif value < a[0]:
        return False

    if value < a[middle_index]:
        return binary_seach(a[0:middle_index],value)
    elif value > a[middle_index]:
        return binary_seach(a[middle_index:], value)
    elif value == a[middle_index]:
        return True




if __name__ == "__main__":
    a = [23,5,6,34,54,78,8,9]

    merge_sort(a)
    print(a)
    # if binary_seach(a,-254):
    #     print('yes')
    # else:
    #     print('no')
