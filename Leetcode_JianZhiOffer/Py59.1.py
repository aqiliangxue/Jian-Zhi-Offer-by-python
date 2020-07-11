class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 解法1 暴力法
        # a=[]
        # if len(nums)<=1:
        #     return nums
        # for i in range(0,len(nums)-k+1):
        #         a.append(max(nums[i:i+k]))
        # return a

        deque = [];result = [] # deque也可以用collection里的双端队列实现
        for i in range(0, len(nums)):
            # 只存有可能成为最大值的数字的index进deque
            if deque and nums[i]>nums[deque[-1]]:
                deque.pop()
            deque.append(i)
            # 如果相距超过窗口k长度，将deque[0]中索引出队
            while i-deque[0]>k-1:
                deque.pop(0)
            if i >= k-1:
                result.append(nums[deque[0]]) # 这过程中始终保持deque[0]为最大值的index
        return result