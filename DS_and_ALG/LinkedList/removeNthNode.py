"""
Yoututbe: https://www.youtube.com/watch?v=tk6fo3Z-qkQ

"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def removeNthNode(head, n):

    # First you need to count the list
    t = 1

    inc = head

    while inc.next:
        t += 1
        inc = inc.next

    k=t - n

    if k == 0:
        #Need to just remove head
        head = head.next
        return head


    inc = head
    prev = None

    # 1-->2-->3-->4-->5
    # k  3   2   1   0

    while k != 0:
        prev = inc
        inc = inc.next
        k -= 1

    prev.next = inc.next

    return head



if __name__ == '__main__':
    # 1->2->3->4->5
    n = 5
    h = ListNode(1)
    h.next = ListNode(2)
    h.next.next = ListNode(3)
    h.next.next.next = ListNode(4)
    h.next.next.next.next = ListNode(5)

    res = removeNthNode(h, n)

    while res:
        print(res.val)
        res = res.next