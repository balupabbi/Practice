
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



def maxDepthT(root):

    if root == None:
        #child of leaf node

        return 0
    else:

        return max(maxDepthT(root.left), maxDepthT(root.right)) + 1

        # if root.left == None and root.right == None:
        #     # at leaf node, both children are None
        #     return max(maxDepthT(root.left), maxDepthT(root.right)) + 1
        #
        #
        #
        # else:
        #     return max(maxDepthT(root.left), maxDepthT(root.right))


# def maxDepthT(root):
#
#     depth = 0
#
#     cn = root
#
#     while cn:
#
#         if cn.left:
#             depth += 1
#         elif cn.right:
#             depth += 1
#
#
#
#     return depth





# 3
# / \
#9   \
#     20
#    /   \
#         15
#   7

if __name__ == '__main__':
    r = TreeNode(3)
    r.left = TreeNode(9)
    r.right = TreeNode(20)
    # r.right.left = TreeNode(15)
    # r.right.right = TreeNode(7)

    print(maxDepthT(r))