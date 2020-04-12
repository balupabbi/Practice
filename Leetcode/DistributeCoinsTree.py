
"""
https://www.geeksforgeeks.org/distribute-candies-in-a-binary-tree/
"""


class TreeNode():

    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None



def distributeCoins(root):
    """
    Returns number of moves
    :param root:
    :return:
    """
    #excess = abs(#ofcoins -1)  = #moves

    if root is None:
        return 0

    l = distributeCoins(root.left)
    r = distributeCoins(root.right)

    excess = abs(root.val - 1)

    return excess


def printTree(root):

    #preorder traversal

    if root:
        print(root.val)
        printTree(root.left)
        printTree(root.right)

if __name__ == '__main__':

    root = TreeNode(3)
    root.right = TreeNode(0)
    root.left= TreeNode(0)

    printTree(root)
    moves = distributeCoins(root)
    print(f"Moves: {moves}")