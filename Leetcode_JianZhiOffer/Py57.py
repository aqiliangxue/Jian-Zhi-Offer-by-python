class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        j=len(nums)-1
        while i<j:
            res=nums[i]+nums[j]
            if target<res:
                j=j-1
            elif target>res:
                i=i+1
            else:
                return nums[i],nums[j]
        # return []