

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def serialize():
    pass

def deserialize():
    pass


"""
Binary Tree 
      1
     /  \
    2    3
   / \     
  4   5   
 /
6
"""
if __name__ == '__main__':
    r = TreeNode(1)
    r.left = TreeNode(2)
    r.right = TreeNode(3)
    r.left.left = TreeNode(4)
    r.left.right = TreeNode(5)
    r.left.left.left = TreeNode(6)