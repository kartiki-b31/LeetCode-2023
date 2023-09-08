class RecentCounter:

    def __init__(self):
        self.arr=[]

    def ping(self, t: int) -> int:
        self.arr.append(t)
        #[1,3001]
        # #for i in range(len(self.arr)):
        #     if (t-3000) <= self.arr[i]:
        #         return len(self.arr)-i
        
        while len(self.arr)>0:
            if (t-3000)<=self.arr[0]:
                return len(self.arr)
            else:
                self.arr.remove(self.arr[0])
            
                

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)