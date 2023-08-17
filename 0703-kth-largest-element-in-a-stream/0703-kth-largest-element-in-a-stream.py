from sortedcontainers import SortedList
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.nums=SortedList(nums)
        
        

    def add(self, val: int) -> int:
        
        self.nums.add(val)
        sc=sorted(self.nums,reverse=True)
        return sc[self.k -1]
        
        
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)