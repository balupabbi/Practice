"""
Given an array of integers, return indices of the two numbers such that they add up to a
specific target.

You may assume that each input would have exactly one solution, and you may not use
the same element twice.
"""





def twoSum(a,target):

    '''
    Brute Force method O(n^2)
    :param a:
    :param target:
    :return:
    '''

    result = []

    for i in range(len(a)):
        for j in range(i+1,len(a)):
            t = a[i] + a[i+1]
            if t == target:
                result.append(i)
                result.append(i+1)
    res = list(set(result))
    return res


def twoSum2(a, target):
    '''
    Hashmap method O(n)
    :param a:
    :param target:
    :return:
    '''

    comp = {} #key=complement of a[i], value=index

    for i in range(len(a)):
        c = target - a[i]
        comp[c]=i

    for key in comp.keys():
        if key in a:
            i1 = a.index(key)
            i2 = comp[key]

            return [i1,i2]


def two_sum(self, nums, target):
    compliments = {}
    result = []
    for index, num in enumerate(nums):
      if compliments.get(num) is None:
        compliments[target-num] = index
      else:
        result = [compliments[num], index]
    return result


if __name__ == '__main__':
    a = [3,4,6,5]
    target = 10

    indexes = twoSum(a,target)
    print(indexes)