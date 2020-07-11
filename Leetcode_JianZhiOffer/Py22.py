# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        a=[]
        tmp=head
        while tmp.next!=None:
            a.append(tmp)
            tmp=tmp.next
        a.append(tmp)
        return a[-k]

        # fomer,latter=head,head
        # # 头指针比后指针多走k步
        # for _ in range(k):
        #     fomer=fomer.next
        # # 前指针为空跳出循环，此时后指针指向要返回的节点
        # while fomer:
        #     fomer=fomer.next
        #     latter=latter.next
        # return latter