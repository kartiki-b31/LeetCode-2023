from collections import deque
class MyStack:
    def __init__(self):
        self.q=deque()
        

    def push(self, x: int) -> None:
        self.q.appendleft(x)


    def pop(self) -> int:
        if len(self.q)!=0: 
            return self.q.popleft()
        

    def top(self) -> int:
        if len(self.q)!=0: 
            return self.q[0]
        
        

    def empty(self) -> bool:
        if len(self.q)!=0:
            return False
        else:
            return True

        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()