class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap=[]
        for i in range(len(nums)):
            heap.append((nums[i],i))
        heapq.heapify(heap)

        while k>0:
            top_ele,idx=heapq.heappop(heap)
            new_ele=top_ele*multiplier
            heapq.heappush(heap,(new_ele,idx))
            nums[idx]=new_ele

            k=k-1

        return nums

