"""
Leetcode: https://leetcode.com/problems/add-two-numbers/

Carry Method Reference: https://www.youtube.com/watch?v=L0xveBXriKc
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    """
    l1 is in reverse order, iterate through it and get a string, reverse string, convert to int, add, reverse sum and convert back to
    linkedlist
    :param self:
    :param l1:
    :param l2:
    :return:
    """
    s1 = ""  # use it as stack to get it in reverse order

    s1 += (str(l1.val))
    while l1.next:
        s1 += (str(l1.next.val))
        l1 = l1.next

    s1_r = s1[::-1]
    s1_r = int(s1_r)

    s2 = ""  # use it as stack to get it in reverse order

    s2 += (str(l2.val))
    while l2.next:
        s2 += (str(l2.next.val))
        l2 = l2.next

    s2_r = s2[::-1]
    s2_r = int(s2_r)

    t = s1_r + s2_r

    t_r = str(t)[::-1]


    head = ListNode(int(t_r[0]))
    curr = head

    for i in range(1,len(t_r)):
        curr.next = ListNode(int(t_r[i]))
        curr = curr.next


    return head



def addTwoNumbersCarry(l1: ListNode, l2: ListNode) -> ListNode:

    c = 0 #carry is initialized to 0
    ans = ListNode(0)
    head = ans

    while l1 or l2:

        if l1.val == None and l2.val == None and c == 0:
            break

        if l1 == None and l2 is not None:
            s = l2.val + c
        elif l2 == None and l1 is not None:
            s = l1.val + c
        else:
            s = l1.val + l2.val + c

        if s >= 10:
            c = 1
        else:
            c = 0

        d = s % 10

        ans.val = d

        if l1 != None:
            l1 = l1.next

        if l2 != None:
            l2 = l2.next

        if l1 or l2:
            ans.next = ListNode(None)
            ans = ans.next



    return head


if __name__ == '__main__':
    n = ListNode(2)
    n.next = ListNode(4)
    n.next.next = ListNode(3)

    n2 = ListNode(5)
    n2.next = ListNode(6)
    n2.next.next = ListNode(4)

    out = addTwoNumbersCarry(n,n2)

    print(out.val)
    while out.next:
        out = out.next
        print(out.val)



