class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i=0
        j=len(nums)-1
        # if len(nums)==1:
        #     return 1
        while i<=j:
            m=(i+j)//2
            # 下标和数组中的值相等
            if nums[m]==m:
                i=m+1
            else:
                j=m-1
        return i