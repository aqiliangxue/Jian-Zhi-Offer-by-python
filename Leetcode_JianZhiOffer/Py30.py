class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.a,self.b =[],[]


    def push(self, x: int) -> None:
        # 将 x 压入栈 A （即 A.add(x) ）；
        # 若 ① 栈 B 为空 或 ② x 小于等于 栈 B 的栈顶元素，则将 x 压入栈 B（即 B.add(x) ）。
        # b[-1]始终为最小值
        self.a.append(x)
        if not self.b or self.b[-1]>=x:
            self.b.append(x)


    def pop(self) -> None:
        # 执行栈 A 出栈（即 A.pop() ），将出栈元素记为 y ；
        # 若 y 等于栈 BB 的栈顶元素，则执行栈 B 出栈（即 B.pop() ）
        if self.a.pop()==self.b[-1]:
            self.b.pop()


    def top(self) -> int:
        # 直接返回栈 A 的栈顶元素即可，即返回 A.peek() 。
        return self.a[-1]


    def min(self) -> int:
        #  直接返回栈 B 的栈顶元素即可，即返回 B.peek() 。
        return self.b[-1]




# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()