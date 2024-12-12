class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap=[-1*n for n in gifts]
        heapq.heapify(heap)

        for i in range(k):
            left=heapq.heappop(heap)
            addi=math.floor(math.sqrt(-1*left))
            heapq.heappush(heap,-1*addi)
        
        #print(heap)
        return -1*int(sum(heap))
