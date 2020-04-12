



def removeElement(nums, val):
    """
    Remove all instances of val in nums and return remaining length of num.
    :return:
    """
    index = 0

    for i, e in enumerate(nums):
        if e != val:
            nums[index] = nums[i]
            index += 1

    return index






if __name__ == '__main__':
    removeElement()