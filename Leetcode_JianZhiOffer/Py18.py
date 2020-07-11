# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:
            return head.next
        pre = head
        tmp = head
        while tmp.val != val:
            pre = tmp
            tmp = tmp.next
        pre.next = tmp.next
        return head

        # if head.val == val: return head.next
        # pre, cur = head, head.next
        # while cur and cur.val != val:
        #     pre, cur = cur, cur.next
        # if cur: pre.next = cur.next
        # return head