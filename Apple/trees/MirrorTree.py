
from collections import deque

class TreeNode():
    def __init__(self,data):
        self.val = data
        self.left = None
        self.right = None


def printTreeLevel(r):
    if not r:
        return

    q = deque()
    q.append(r)

    while q:
        cn = q.popleft()
        print(cn.val)
        #check neighbors
        if cn.left and cn.right:
            q.append(cn.left)
            q.append(cn.right)
        elif cn.left and cn.right is None:
            q.append(cn.left)
        elif cn.right and cn.left is None:
            q.append(cn.right)

def mirrorTree(r1):

    #level order traversal using queue

    if not r1:
        return

    q = deque()
    q.append(r1)

    """
    [200,50]
    """
    while q:
        cn = q.popleft()
        #print(cn.val)
        #check neighbors
        if cn.left and cn.right:
            #switch
            tmpn= cn.left
            cn.left = cn.right
            cn.right = tmpn

            q.append(cn.left)
            q.append(cn.right)

        elif cn.left and cn.right is None:
            tmpn = cn.left
            cn.right = tmpn
            cn.left = None
            q.append(cn.right)

        elif cn.right and cn.left is None:
            tmpn = cn.right
            cn.left = tmpn
            cn.right = None
            q.append(cn.left)

    printTreeLevel(r1)

    return



"""




"""

if __name__ == '__main__':
    t = TreeNode(20)
    t.left = TreeNode(50)
    t.right = TreeNode(200)
    t.left.left = TreeNode(75)
    t.left.right = TreeNode(25)
    t.right.right = TreeNode(300)

    # t2 = TreeNode(20)
    # t2.left = TreeNode(200)
    # t2.right = TreeNode(50)
    # t2.right.left = TreeNode(25)
    # t2.right.right = TreeNode(75)
    # t2.left.left = TreeNode(300)

    mirrorTree(t)