
class TreeNode():
    def __init__(self,data):
        self.val = data
        self.left = None
        self.right = None




def checkIdentical(r1,r2):

    def isIdentical(r1,r2):
        """
        preorder traversal
        :param r1:
        :param r2:
        :return:
        """

        if r1 is None and r2 is None:
            return True
        elif r1 is None and r2 is not None:
            return False
        elif r1 is not None and r2 is None:
            return False
        else:
            #check left subtree, current value and right subtree

            lc = isIdentical(r1.left,r2.left)

            if r1.val != r2.val:
                cc = False
            else:
                cc = True

            rc = isIdentical(r1.right,r2.right)

            return (lc and cc and rc)




    return isIdentical(r1,r2)






"""
     10
    /  \
   5    15
  /
 4
"""

if __name__ == '__main__':
    t = TreeNode(10)
    t.left = TreeNode(5)
    t.right = TreeNode(15)
    t.left.left = TreeNode(4)
    # t.left.right = TreeNode(6)

    t2 = TreeNode(10)
    t2.left = TreeNode(5)
    t2.right = TreeNode(15)
    t2.left.left = TreeNode(4)

    #checkIdentical(t,t2)
    #print(checkIdentical(t,t2))
    if checkIdentical(t,t2):
        print('Yes Identical')
    else:
        print('No it isnt identical')