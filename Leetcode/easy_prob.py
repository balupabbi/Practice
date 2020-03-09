

def find_peak_element(a,iterative,recursive,linear):

    if iterative == True:
        print("Iterative approach")

    elif recursive == True:
        print("Recursive approach")

        mid = int((len(a)-1)/2)

        if a[mid] > a[mid+1]:
            #search left side because peak is on the left side
            find_peak_element(a[:mid+1], iterative=False, recursive=True, linear=False)
        elif a[mid] < a[mid+1]:
            #search right side because peak is on the right side
            find_peak_element(a[mid+1:],iterative=False, recursive=True, linear=False)


    elif linear == True:
        print("linear approach")

        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                return a[i]

        return (a[len(a)-1])

    return


def rotate_array():
    """

    :return:
    """
    nums = [1,2,3,4,5,6,7]
    k = 3

    if len(nums) == 0:
        return

    rms = nums

    remainder = len(nums) % k

    for i in range(0, len(nums)):
        rms[i + remainder] = nums[i]

    return rms

def buy_sell_stock():
    """
    https://www.youtube.com/watch?v=mj7N8pLCJ6w
    https://www.youtube.com/watch?v=blUwDD6JYaE
    [7,1,5,3,6,4]
    :return:
    """

    stocks = [7,1,5,3,6,4]
    for i in range(0,len(stocks)):
        print (stocks[i])

def remove_dup(arr):
    """
    arr = [2,2,3,4,5,5,5,6]
    :param arr:
    :return:
    """
    i = 1
    for j in range(2,len(arr)):
        if arr[i] != arr[j]:
            arr[i] = arr[j]
            i = i+1
    print(arr[:i])

def merge(nums1, m, nums2, n) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    if len(nums2) == 0 or len(nums1) == 0:
        return nums1

    p1 = (m - 1)
    p2 = len(nums2) - 1
    p3 = len(nums1) - 1

    while True:
        if p2 == -1:
            break
        else:
            if nums1[p1] < nums2[p2]:

                nums1[p3] = nums2[p2]
                p2 = p2 - 1
                p3 = p3 - 1

            elif nums1[p1] > nums2[p2]:

                nums1[p3] = nums1[p1]

                if p1 != 0:
                    p1 = p1 - 1
                elif p1 == 0:
                    nums1[p1] = nums2[p2]
                    p2 = p2 -1

                p3 = p3 - 1

            elif nums1[p1] == nums2[p2]:
                print(p1)
                print(p2)
                nums1[p3] = nums1[p1]
                nums1[p3 - 1] = nums2[p2]
                p1 = p1 - 1
                p2 = p2 - 1
                p3 = p3 - 2

        n = n - 1

    return nums1


if __name__ == "__main__":

    a=[1,2,1,3,5,0]
    a=[1,1,1]
    a=[19,12,1]
    print(find_peak_element(a,iterative=False,recursive=False,linear=True))









    # #rotate_array()
    # #buy_sell_stock()
    # #remove_dup(arr)
    #
    # #nums1 = [1, 2, 3, 0, 0, 0]
    # nums1 = [0,0,0,0,0,0]
    # m = 1
    # #nums2 = [2, 5, 6]
    # nums2 = [1,2,3,4,5]
    # n = 1
    #
    # print(merge(nums1,m,nums2,n))