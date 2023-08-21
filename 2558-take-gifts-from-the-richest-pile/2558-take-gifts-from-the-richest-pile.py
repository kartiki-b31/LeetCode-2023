import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
#         for i in range(k):
#             max_index=gifts.index(max(gifts))
#             gifts[max_index]=math.floor(math.sqrt(gifts[max_index]))
            
            
#         return int(sum(gifts))
        gifts=[-1*i for i in gifts]
        heapq.heapify(gifts)
        #print(gifts)
        
        for i in range(k):
            top_element=heapq.heappop(gifts)
            #print(gifts)
            sqrt_top_element=math.floor(math.sqrt(-1*top_element))
            heapq.heappush(gifts, -1*sqrt_top_element)
            
        
        return -1*int(sum(gifts))
            