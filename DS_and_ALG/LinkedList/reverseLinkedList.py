class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



def reverseLL(head):
    """
    use queue  Time Complexity = O(n) and Space Complexity = O(n)
    :param head:
    :return:
    """

    s = []

    ptr = head

    while ptr:
        s.append(ptr)
        ptr = ptr.next

    #[1,2,3,4,5]

    cn = s.pop()
    ptr = cn

    while s:
        ptr.next = s.pop()# 4, 4.next = 5Node
        ptr.next.next = None
        ptr = ptr.next


    #Node-> 5 -> 4 -> 3-> 2-> 1

    return cn



def reverseLL2(head):
    """
    Iterative approach, Time Complexity O(n)
    :param head:
    :return:
    """

    # 1, 2,3,4,5 ===> 5,->4,->3,->2,->1,->None   |

    #c.next = None   #c=1
    #c.next = prev   #c=2   iterate until c is None

    prev = None
    curr = head


    while curr:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode

    return prev

















if __name__ == '__main__':
    # 1->2->3->4->5
    h = ListNode(1)
    h.next = ListNode(2)
    h.next.next = ListNode(3)
    h.next.next.next = ListNode(4)
    h.next.next.next.next = ListNode(5)

    res = reverseLL2(h)

    while res:
        print(res.val)
        res = res.next
