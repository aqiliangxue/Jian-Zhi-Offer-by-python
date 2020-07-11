class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 解法1
        # n=0
        # if target not in nums:
        #     return 0
        # for i in nums:
        #     if i==target:
        #         n=n+1
        #     if i>target:
        #         break
        # return n

        # 解法2
        # first=0
        # last=len(nums)-1
        # n=0
        # i=1
        # found=False
        # if nums==[]:
        #     return 0
        # while first<=last and not found:
        #     mid=(last+first)//2
        #     if nums[mid]==target:
        #         n=n+1
        #         found=True
        #     else:
        #         if nums[mid]<target:
        #             first=mid+1
        #         else:
        #             last=mid-1
        # if mid +i <= len(nums)-1:
        #     while nums[mid+i]==target :
        #         n=n+1
        #         if mid+i+1 <= len(nums)-1:
        #             i=i+1
        #         else:
        #             break

        # i=1
        # if mid-i>=0:
        #     while nums[mid-i]==target:
        #         n=n+1
        #         if mid-i-1>=0:
        #             i=i+1
        #         else:
        #             break
        # return n

        # 解法3,探索左右界
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            # 搜索右界
            if nums[m] <= target:
                i = m + 1
            else:
                j = m - 1
        right = i
        i = 0

        while i <= j:
            # 搜索左界
            m = (i + j) // 2
            if nums[m] >= target:
                j = m - 1
            else:
                i = m + 1
        left = j
        return right - left - 1