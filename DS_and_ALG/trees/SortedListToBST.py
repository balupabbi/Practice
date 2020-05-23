"""
https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
109. Convert Sorted List to Binary Search Tree
"""


class TreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def listToBST(a):
    """
    sorted a, use binary search methodology
    :return:
    """
    s = 0
    e = len(a) -1
    #root = convertBST(a,s,e)
    root = convertBST2(a)

    return root

"""
[2,4,10,15,20]
mid = 5//2=2=>10
mid = 2//2 = 1 ==>4
mid = 1//2 = 0
"""

def convertBST2(a):
    if not a:
        return None

    mid = len(a)//2
    root = TreeNode(a[mid])
    root.left = convertBST2(a[:mid])
    root.right = convertBST2(a[mid+1:])

    return root

def convertBST(a,s,e):

    #base case
    if s > e:
        return None

    mid = s+(e-s)//2

    root = TreeNode(a[mid])
    root.left = convertBST(a,s,mid-1)
    root.right = convertBST(a,mid+1,e)

    return root


if __name__ == '__main__':
    a = [2,4,10,15,20]

    r = listToBST(a)
    print(r.data)
    print(r.left.data,r.right.data)

    print(r.left.left.data, r.right.left.data)

