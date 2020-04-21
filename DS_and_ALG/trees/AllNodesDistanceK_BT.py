"""
leetcode: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

Reference: https://www.youtube.com/watch?v=nPtARJ2cYrg
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None




# def distanceK(root: TreeNode, target: TreeNode, K: int):
#
#     ans = []
#     i = 0   # calculates distance going downward, traverses until K
#     level = 0
#
#     queue = []
#     queue.append([target,level])
#
#     while queue:
#         ce = queue.pop(0)
#         cn = ce[0]
#         cl = ce[1]
#
#         if cl == K:
#             ans.append(cn.val)
#
#
#         if cn.left is not None and cn.right is not None:
#             level += 1
#             queue.append([cn.left,level])
#             queue.append([cn.right,level])
#         elif cn.left is not None:
#             level += 1
#             queue.append([cn.left,level])
#         elif cn.right is not None:
#             level += 1
#             queue.append([cn.right,level])
#
#
#         # i+=1
#
#
#     return ans
#     # def preorder(start, i):
#     #     print(start.val)
#     #     preorder(start.left)
#     #     preorder(start.right)
#     #
#     # start = target
#     # preorder(start,K)
#
#
#     pass


def distanceK(root: TreeNode, target: TreeNode, K: int):
    """

    :param root:
    :param target:
    :param K:
    :return:
    """
    #First populate hashtable with Key=node.val, Value=Parent node val

    parents = {}

    def preorder(start):

        if start.left:
            parents[start.left.val] = start
            preorder(start.left)

        if start.right:
            parents[start.right.val] = start
            preorder(start.right)

    preorder(root)

    #Start from target node and move up level by level until level = K
    # As you move up the level
    seen = []
    queue = []
    level = 0

    queue.append(target)

    while queue:
        if level == K:
            return [x.val for x in queue]
            #return queue



        size = len(queue)

        for i in range(size):
            cn = queue.pop(0)

            if cn.val not in seen:
                #we haven't seen this node and needs to be processed
                #get parent, left and right child add to queue
                if cn.left:
                    if cn.left.val not in seen:
                        queue.append(cn.left)

                if cn.right:
                    if cn.right.val not in seen:
                        queue.append(cn.right)

                if cn.val in parents:
                    if parents[cn.val].val not in seen:
                        queue.append(parents[cn.val])

                seen.append(cn.val)

        level += 1


    pass


if __name__ == '__main__':
    t = TreeNode(3)
    t.left = TreeNode(5)
    t.right = TreeNode(1)
    t.right.left = TreeNode(0)
    t.right.right = TreeNode(8)
    t.left.left = TreeNode(6)
    t.left.right = TreeNode(2)
    t.left.right.left = TreeNode(7)
    t.left.right.right = TreeNode(4)


    print(distanceK(t,t.left,2))

