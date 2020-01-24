



#Input is an array of integer and you have to reorder them so even appear first
def even_odd(A):
    next_even, next_odd = 0, len(A) -1

    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1

    return A








if __name__ == "__main__":
    arr = [2,3,4,21,45,66,87]
    res = even_odd(arr)
    print (res)