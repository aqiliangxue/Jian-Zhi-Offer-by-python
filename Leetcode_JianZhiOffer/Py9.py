class CQueue:

    def __init__(self):
        self.a = []
        self.b = []

    def appendTail(self, value: int) -> None:
        self.a.append(value)

    def deleteHead(self) -> int:

        # 如果b有值，每次将b中值出栈
        if self.b:
            return self.b.pop()
        # 如果b为空，且a为空，返回-1
        if self.a == []:
            return -1
        # 将a中元素倒序，实现队列功能
        while self.a:
            # b中元素实现a中元素倒序
            self.b.append(self.a.pop())
        return self.b.pop()

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()