# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 归并排序
        # b为头指针，不会被更新
        a=b=ListNode(0)
        while l1 and l2:
            if l1.val >= l2.val:
                a.next=l2
                l2=l2.next
            else:
                a.next=l1
                l1=l1.next
            # 更新a的指针
            a=a.next
        # 如果某个链表有剩余，直接加到末尾
        a.next=l1 if l1 else l2
        return b.next