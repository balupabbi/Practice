from collections import defaultdict
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def levelOrder(root: TreeNode):
    q = []
    level = 0
    q.append((root, level))
    ans = defaultdict(list)

    while q:
        c = q.pop(0)

        n = c[0]
        level = c[1]

        ans[level].append(n.val)

        # check and append neighbors
        if n.left and n.right:
            n_left = n.left
            n_right = n.right
            level += 1
            q.append((n_left, level))
            q.append((n_right, level))
        elif n.left:
            n_left = n.left
            level += 1
            q.append((n_left, level))
        elif n.right:
            n_right = n.right
            level += 1
            q.append((n_right, level))

    out = [[] for i in range(len(ans))]

    for k, v in ans.items():
        out[k] = v

    return out




ans = deque()

def levelOrderRecursive(root:TreeNode):

    level = 0

    def helper(root, ans, level):

        if not root:
            return
        else:
            if len(ans) < level + 1:
                ans.append([])
            ans[level].append(root.val)

            # ans[level].append(root.val)

            helper(root.left,ans, level+1)
            helper(root.right, ans, level+1)

    helper(root,ans,level)

    return ans

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
    r.right.left = TreeNode(15)
    r.right.right = TreeNode(7)

    #print(levelOrder(r))
    print(levelOrderRecursive(r))