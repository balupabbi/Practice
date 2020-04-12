"""
Given a binary tree, Write a function to test if tree is binary search tree or not
"""

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree():
    def __init__(self,root):
        self.root = root

    def isBST(self, root):
        """
        Checks if tree is binary searchTree,
        if left child is less than right child then its a binary search tree
        :param start:
        :return:
        """

        """
        All the cases that we need to check
        - start node is None
        - Duplicate values in the tree like right and left value are same
        - each Node value is only valid if it is between min and max
        """

        '''
             5  min=-infinity, max = infinity      
            / \
           3   7 min = 5, max = infinity
min=-infinity max = 5            
        '''
        return self.helperBST(root, float("-inf"), float("inf"))






    def helperBST(self, root, min, max):

        if root is None:
            return True
        elif root.value <= min or root.value >= max:
            return False
        validRightTree = self.helperBST(root.right, root.value, max)
        validLeftTree = self.helperBST(root.left, min, root.value)

        return validLeftTree and validRightTree
















if __name__ == '__main__':
    a = Node(5)
    a.left = Node(1)
    a.right = Node(7)
    a.right.left = Node(6)
    a.right.right = Node(8)

    t = Tree(a)

    if t.isBST(a):
        print ('yes')
    else:
        print('no')

