
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        minheap=nums[:k]
        heapq.heapify(minheap)
        print(minheap)
        for i in nums[k:]:
            if i>minheap[0]:
                heappop(minheap)
                heappush(minheap,i)

        return heappop(minheap)

