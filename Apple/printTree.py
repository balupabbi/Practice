
# Print out the data of a binary tree structure. From left to right if the level is odd and right to left if the level is even.
#
#

from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



   #      9         Level 1     9
   #    /   \
   #   7     20     Level 2  20,7
   #  / \     / \
   # 3   5   10  25   Level 3   3,5,10,25
#  / \  / \ / \  / \
# 1   4 4 6 8 12 22 26  Level 4

def printTreeZigZagIterative(start):
    """
    left to right = odd
    right to left = even

    utilize s1
    utilize s2
    :param start:
    :return:
    """

    s1 = deque()
    s2 = deque()

    #start with root node
    s1.append(start)

    out = []

    while s1 or s2:

        while s1:
            cn = s1.pop()

            #left right append

            if cn.left:
                s2.append(cn.left)

            if cn.right:
                s2.append(cn.right)

            out.append(cn.val)


        while s2:
            cn = s2.pop()

            #right left append

            if cn.right:
                s1.append(cn.right)

            if cn.left:
                s1.append(cn.left)

            out.append(cn.val)

    return out









def preorder_traversal(start):

    if not start:
        return

    print(start.val)
    preorder_traversal(start.left)
    preorder_traversal(start.right)


def inorder_traversal(start):

    if not start:
        return

    inorder_traversal(start.left)
    print(start.val)
    inorder_traversal(start.right)

def postorder_traversal(start):

    if not start:
        return

    postorder_traversal(start.left)
    postorder_traversal(start.right)
    print(start.val)

#Recursive Way: https://www.geeksforgeeks.org/level-order-tree-traversal/
def levelOrderTraversal(start):
    q = deque()
    level = 1
    q.append((start,level))
    out = []

    while q:
        cn,level = q.popleft()
        out.append((cn.val,level))

        level += 1
        if cn.left:
            q.append((cn.left, level))

        if cn.right:
            q.append((cn.right,level))

    return out


def leftRightOrderTraversal(start):

    if not start:
        return

    q = deque()
    out = []

    out.append(start.val)

    if start.left and start.right:
        q.append(start.left)
        q.append(start.right)
    elif not start.left or not start.right:
        return out


    while q:

        f = q.popleft()
        s = q.popleft()

        if f.left and s.right:
            q.append(f.left)
            q.append(s.right)

        if f.right and s.left:
            q.append(f.right)
            q.append(s.left)

        out.append(f.val)
        out.append(s.val)

    return out



def findHeight(start):

    def helper(start):
        if not start:
            return 0
        else:

            lc = helper(start.left)
            rc =  helper(start.right)

            return 1+max(lc,rc)

    return helper(start)



   #      9         Level 1   right to left      4
   #    /   \
   #   7     20     Level 2   left to right      3
   #  / \     / \
   # 3   5   10  25   Level 3    right to left    2
#  / \  / \ / \  / \
# 1   4 4 6 8 12 22 26                            1


   #  [7,20,3,5,10,25

if __name__ == "__main__":
    r = TreeNode(9)
    r.left = TreeNode(7)
    r.right = TreeNode(20)
    r.left.left = TreeNode(3)
    r.left.right = TreeNode(5)
    r.right.left = TreeNode(10)
    r.right.right = TreeNode(25)

    r.left.left.left = TreeNode(1)
    r.left.left.right = TreeNode(4)
    r.left.right.left = TreeNode(4)
    r.left.right.right = TreeNode(6)

    r.right.left.left = TreeNode(8)
    r.right.left.right = TreeNode(12)
    r.right.right.left = TreeNode(22)
    r.right.right.right = TreeNode(26)


    # preorder_traversal(r)
    # print("------------------")
    # inorder_traversal(r)
    # print("------------------")
    # postorder_traversal(r)

    #print(levelOrderTraversal(r))

    # print (leftRightOrderTraversal(r))
    #print(findHeight(r))
    print(printTreeZigZagIterative(r))