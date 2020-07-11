# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        s=[]
        if head !=None:
            while head.next :
                s.append(head.val)
                head=head.next
            s.append(head.val)
        return s[::-1]