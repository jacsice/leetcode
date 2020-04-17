# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        cur = head
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if not l1:
            cur.next = l2
        if not l2:
            cur.next = l1
        return head.next


if __name__ == '__main__':
    solution = Solution()
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(4)
    n4 = ListNode(1)
    n5 = ListNode(3)
    n6 = ListNode(4)
    n1.next = n2
    n2.next = n3

    n4.next = n5
    n5.next = n6
    n = solution.mergeTwoLists(n1, n4)
    while n:
        print(n.val)
        n = n.next
