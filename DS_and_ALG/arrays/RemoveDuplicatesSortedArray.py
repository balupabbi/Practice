




from collections import defaultdict



def removeDuplicatesSortedArray(nums):

    return list(set(nums))

def removeDuplicatesSortedArray2(nums):
    """
    Not in place
    :param nums:
    :return:
    """
    count = defaultdict(int)

    for n in nums:
        count[n] += 1


    return list(count.keys())


def removeDuplicatesSortedArray3(nums):
    """
    in plce
    :param nums:
    :return:
    """
    i = 0

    for j in range(1,len(nums)):
        # compare i and j

        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]



    return nums[:i+1]




if __name__ == "__main__":
    nums = [1, 1, 2]
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

    print(removeDuplicatesSortedArray3(nums))