# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 爱的相遇
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node1, node2 = headA, headB

        while node1 != node2:
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA
        return node1

        # 空间复杂度超过O(1)
        # n1,n2=headA,headB
        # s=set()
        # while n1:
        #     s.add(n1)
        #     n1=n1.next
        # l=len(s)
        # while(n2):
        #     s.add(n2)
        #     if len(s)==l:return n2
        #     else:l=l+1
        #     n2=n2.next
        # return None