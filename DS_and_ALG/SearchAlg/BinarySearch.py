
def binarySearch (arr, l, r, x):

    # Check base case
    if r >= l:

        mid = l + (r - l )//2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

            # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid -1, x)

            # Else the element can only be present in right subarray
        else:
            return binarySearch(arr, mid +1, r, x)

    else:
        # Element is not present in the array
        return -1


def binarySearch2(arr, l, r, x):
    """
    iterative approach
    :param arr:
    :param l:
    :param r:
    :param x:
    :return:
    """
    while l <= r:

        mid = l + (r - l) // 2;

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

            # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1

        # If x is smaller, ignore right half
        else:
            r = mid - 1

    # If we reach here, then the element was not present
    return -1







if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10

    result = binarySearch(arr, 0, len(arr) - 1, x)



    if result != -1:
        print("Element is present at index {}".format(result))
    else:
        print("Element is not present in array")