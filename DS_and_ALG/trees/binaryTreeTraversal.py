#Slides: https://docs.google.com/presentation/d/1OPqeIRnRyYLpFQPk7Wf0qmCUe-cMmAsI1hUqpab0B_s/edit#slide=id.p
#Tutorial Youtube: https://www.youtube.com/watch?v=6oL-0TdVy28&list=PL5tcWHG-UPH2fmYC6kgey1RIxP2iK9EEL&index=2&t=0s


from collections import deque


class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



class BinaryTree():
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, start, traversal_type):

        if traversal_type == 'preorder':
            print('Preorder: ' + self.preorder(start, ''))
        elif traversal_type == 'inorder':
            print('Inorder: ' + self.inorder(start,''))
        elif traversal_type == 'postorder':
            print('Postorder: ' + self.postorder(start,''))
        elif traversal_type == 'levelorder':
            print('Levelorder: ' + self.levelorder(start, ''))
        elif traversal_type == 'reverselevelorder':
            print('Reverselevelorder: ' + self.reverselevelorder(start,''))
        else:
            print("Invalid")

        return

    def preorder(self, start, traversal):
        """
        Recursive method
        :param start:
        :return:
        """
        #root-->left->right
        #print('yes')

        if start:
            traversal = traversal + str(start.value) + '-->'
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)

        return traversal

    def inorder(self,start, traversal):
        #left -> root -> right

        if start:
            traversal = self.inorder(start.left, traversal)
            traversal = traversal + str(start.value) + '-->'
            traversal = self.inorder(start.right, traversal)

        return traversal

    def postorder(self,start, traversal):
        #left -> right -> root

        if start:
            traversal = self.postorder(start.left, traversal)
            traversal = self.postorder(start.right, traversal)
            traversal = traversal + str(start.value) + '-->'

        return traversal

    def levelorder(self,start,traversal):
        """
        Use queue
        :param start:
        :return:
        """
        if start is None:
            return

        queue = deque()
        queue.append(start)

        while queue:

            current_node = queue.popleft()

            traversal = traversal + str(current_node.value) + '-->'

            if current_node.left:
                queue.append(current_node.left)

            if current_node.right:
                queue.append(current_node.right)

        return traversal

    def reverselevelorder(self,start, traversal):
        """
        # s = [2,4,3,5,8,6]
# q = [2], [4,3], [3,5], [5,8,6], [8,6]

        Uses queue and stack
        :param start:
        :param traversal:
        :return:
        """

        stack = []
        queue = deque()

        if start:
            queue.append(start)
        else:
            return traversal

        while queue:
            c_node = queue.popleft()
            stack.append(c_node.value)

            if c_node.right:
                queue.append(c_node.right)

            if c_node.left:
                queue.append(c_node.left)

        while stack:
            traversal = traversal + str(stack.pop()) + '-->'

        return traversal

    def height(self, node):
        """
        Utilizes recursive call
        :param node:
        :return:
        """

        if not node:
            return -1

        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return 1+(max(left_height,right_height))

    def sizeoftree(self,node):
        """
        Uses iterative approach with stack
        :param root:
        :return:
        """
        stack = []
        count = 0

        if not node:
            return count

        stack.append(node)

        while stack:
            node_c = stack.pop()
            count += 1

            if node_c.left:
                stack.append(node_c.left)
            if node_c.right:
                stack.append(node_c.right)

        return count

    def sizeoftree2(self,node):
        """
        Recursive approach
        :param node:
        :return:
        """

        if not node:
            return 0
        return 1+self.sizeoftree2(node.left)+self.sizeoftree2(node.right)

#     2
#    /  \
#   3    4
#  / \  / \
# 6   8 5
# Preorder: 2-->3-->6-->8-->4-->5-->
# Inorder: 6-->3-->8-->2-->5-->4-->
# Postorder: 6-->8-->3-->5-->4-->2-->
# Levelorder: 2-->3-->4-->6-->8-->5-->
# Reverselevelorder: 6-->8-->5-->3-->4-->2-->
# 0
# 6
# 6

if __name__ == '__main__':

    tree = BinaryTree(2)
    tree.root.left = Node(3)
    tree.root.right = Node(4)
    tree.root.left.left = Node(6)
    tree.root.left.right = Node(8)
    tree.root.right.left = Node(5)

    tree.print_tree(tree.root, 'preorder')
    tree.print_tree(tree.root, 'inorder')
    tree.print_tree(tree.root, 'postorder')
    tree.print_tree(tree.root, 'levelorder')
    tree.print_tree(tree.root, 'reverselevelorder')

    print(tree.height(tree.root.left.left))
    print(tree.sizeoftree(tree.root))
    print(tree.sizeoftree2(tree.root))