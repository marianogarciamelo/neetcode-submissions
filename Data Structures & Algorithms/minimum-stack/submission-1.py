class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
       self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        minStack = []
        for s in self.stack:
            if not minStack:
                minStack.append(s)
            elif minStack and s < minStack[-1]:
                minStack.pop()
                minStack.append(s)
            else: s += 1
        return minStack[0]
        
