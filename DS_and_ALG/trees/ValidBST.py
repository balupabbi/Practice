"""
Leetcode: https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/625/

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isValidBST(root: TreeNode) -> bool:
    """
    Iterative approach
    :param self:
    :param root:
    :return:
    """
    visited = []
    s = []
    s.append(root)

    while s:
        cn = s.pop()

        if cn not in visited:
            cv = cn.val

            if cn.left and cn.right:
                lv = cn.left.val
                rv = cn.right.val

                if cv < lv or cv > rv:
                    return False

                #add left and right nodes in stack
                s.append(cn.left)
                s.append(cn.right)

            visited.append(cn)
        else:
            continue

    return True



def isValidBST(root):
    """
    Recursive way
    :return:
    """

    if root == None:
        return True



if __name__ == '__main__':
    r = TreeNode(3)
    r.left = TreeNode(9)
    r.right = TreeNode(20)
    r.right.left = TreeNode(15)
    r.right.right = TreeNode(7)

    r1 = TreeNode(2)
    r1.left = TreeNode(1)
    r1.right = TreeNode(3)

    r2 = TreeNode(5)
    r2.left = TreeNode(1)
    r2.right = TreeNode(4)
    r2.right.left = TreeNode(3)
    r2.right.right = TreeNode(6)

    if isValidBST(r2):
        print("Valid Binary Tree")
    else:
        print("Invalid Binary Tree")