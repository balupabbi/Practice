


# 53-54 = 1
# abs(a-b)
#
# 71-68 = 3
#
# 71-(-70) = huge
# -70-71 = huge
#
# -70-(-72) = 1
# sort  -72 -70 -3,1,17,68,71
#
#
# 1,3,17,68,70,71,72
#
# sort it and check difference between arr[last]-arr[secondlast] and store it in s




#O(nlogn) solution

def minimumAbsoluteDifference(arr):

    if not arr:
        return

    # arr = [abs(i) for i in arr]

    arr.sort()

    mindiff=74848474848



    for i in range(len(arr)):

        if (i+1)>len(arr)-1:
            break

        mindiff = min(mindiff,(arr[i+1]-arr[i]))
        # if arr[i+1]-arr[i] < mindiff:
        #     mindiff = arr[i+1]-arr[i]





    return mindiff


if __name__ == '__main__':
    arr = [-72, -70, -3,1,17,68,71]

    #arr = [1, -3, 71, 68, 17]
    #1,3,17,68,71
    print(minimumAbsoluteDifference(arr))