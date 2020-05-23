from collections import Counter



def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    m = {}
    if len(nums1 ) <len(nums2):
        nums1 ,nums2 = nums2 ,nums1
    for i in nums1:
        if i not in m:
            m[i] = 1
        else:
            m[i] += 1
    result = []
    for i in nums2:
        if i in m and m[i]:
            m[i] -= 1
            result.append(i)
    return result

def intersect2(nums1, nums2):
    if not nums1 or not nums2:
        return []

    n1 = {}

    for i in nums1:
        if i not in n1:
            n1[i] = 1
        else:
            n1[i] += 1

    n2 = {}

    for i in nums2:
        if i not in n2:
            n2[i] = 1
        else:
            n2[i] += 1

    intersection = []

    for k in n1:
        if k in n2:
            for times in range(min(n1[k], n2[k])):
                intersection.append(k)

    return intersection

def intersect3( nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    nums1, nums2 = sorted(nums1), sorted(nums2)
    p1 = p2 = 0
    ans = []
    while p1 < len(nums1) and p2 < len(nums2):
        if nums1[p1] < nums2[p2]:
            p1 += 1
        elif nums1[p1] > nums2[p2]:
            p2 += 1
        else:
            ans += nums1[p1],
            p1 += 1
            p2 += 1
    return ans


def intersect4(nums1,nums2):
    res = []
    n1 = Counter(nums1)
    n2 = Counter(nums2)
    intersections = set(nums1) & set(nums2)
    for i in intersections:
        res.extend(min(n1[i], n2[i]) * [i])
    return res



if __name__ == '__main__':
    nums1 = [1, 4, 5, 3, 6]
    nums2 = [2, 3, 5, 7, 9]

    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]

    print(intersect4(nums1,nums2))










