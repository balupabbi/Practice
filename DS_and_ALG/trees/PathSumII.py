"""
https://leetcode.com/problems/path-sum-ii/
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def pathSum(root: TreeNode, total: int):
    # 22,

    # root node definitely counts
    # DFS approach either recursive or stack
    if not root:
        return

    paths = []

    def findPath(root, total, cp):

        if not root:
            return

        if not root.left and not root.right and total == root.val:
            cp.append(root.val)
            paths.append(cp[:])
            return

        total -= root.val
        cp.append(root.val)
        findPath(root.left, total, cp[:])
        findPath(root.right, total, cp[:])

    cp = []
    findPath(root, total, cp)

    return paths





"""
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1


"""



if __name__ == '__main__':
    r = TreeNode(5)
    r.left = TreeNode(4)
    r.right = TreeNode(8)

    r.left.left = TreeNode(11)
    r.left.left.left = TreeNode(7)
    r.left.left.right = TreeNode(2)


    r.right.left = TreeNode(13)
    r.right.right = TreeNode(4)
    r.right.right.left = TreeNode(5)
    r.right.right.right = TreeNode(1)

    print(pathSum(r, 22))
