class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        sc=sorted(stones)
        
        for i in range(len(sc)):
            sc.sort()
            if len(sc)>1:
                y=sc.pop()
                x=sc.pop()
                
                if y!=x:
                    sc.append(y-x)
            
        if sc:
            return sc[0]
                    
                
        return 0
                