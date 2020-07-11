
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
            # 字典中某一个数字出现次数大于等于2就退出
            if d[i]>=2:
                return i