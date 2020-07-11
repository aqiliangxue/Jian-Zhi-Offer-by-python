# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 解法1
        # a=[]
        # # root=ListNode(1)
        # tmp1=head
        # while tmp1!= None:
        #     a.append(tmp1.val)
        #     tmp1=tmp1.next

        # tmp=head
        # while tmp!=None:
        #     tmp.val=a.pop()
        #     tmp=tmp.next

        # return head

        # 解法2 三指针法
        if head is None or head.next is None:
            return head

        prev, cur = head, head.next
        prev.next = None

        while cur:
            # 保存当前节点的next
            cur_next = cur.next
            # 实现两个节点翻转
            cur.next = prev
            prev = cur
            # 移到下一节点
            cur = cur_next

        return prev