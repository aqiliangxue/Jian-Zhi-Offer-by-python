class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack,i=[],0
        for num in pushed:
            stack.append(num)
            while stack and stack[-1]==popped[i]:#循环判断与出栈
                stack.pop()
                i=i+1
        return not stack