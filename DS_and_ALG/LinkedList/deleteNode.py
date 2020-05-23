class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None




def deleteNode(n,val):
    """
    N is starting point of Linked list, val is the value needs to be deleted
    :param n:
    :param val:
    :return:
    """

    if not n:
        return n

    head = n
    prev_n = None

    while n:
        c_node = n

        if c_node == head and c_node.val == val:
            head = c_node.next
            n = n.next
        elif c_node.val == val:
            #Assuming middle or end
            prev_n.next = c_node.next
            n = n.next
        else:
            prev_n = c_node
            n = n.next




    return head


def deleteNode2(node):
    """
    node is node that needs to get deleted
    :param node:
    :return:
    """

    node.val = node.next.val
    node.next = node.next.next





if __name__ == '__main__':
    n = ListNode(2)
    n.next = ListNode(4)
    n.next.next = ListNode(3)

    n = deleteNode(n,4)

    while n:
        print(n.val)
        n = n.next
