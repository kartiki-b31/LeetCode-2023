
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n=len(nums)
        minheap=[]

        for i in range(len(nums)):
            minheap.append(-nums[i])
        
        heapq.heapify(minheap)
        print(minheap)
        while k>0:
            res=minheap.pop(0)
            heapq.heapify(minheap)
            k-=1

        return -res

