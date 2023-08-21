import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        for i in range(k):
            max_index=gifts.index(max(gifts))
            gifts[max_index]=math.floor(math.sqrt(gifts[max_index]))
            
            
        return int(sum(gifts))
        