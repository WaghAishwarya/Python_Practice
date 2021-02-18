# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1 : ListNode, l2 : ListNode) -> ListNode:
        x = ListNode(0)
        head = x

        while l1 != None and l2 != None:

            if l1.val < l2.val:
                x.next = l1
                l1 = l1.next

            else:
                x.next = l2
                l2 = l2.next

            x = x.next

        if l1 == None:
            x.next = l2
        else:
            x.next = l1

        return head.next


