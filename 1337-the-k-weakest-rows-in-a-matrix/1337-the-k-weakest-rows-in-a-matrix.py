import heapq
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heapa=[]
        res=[]
        heapq.heapify(heapa)
        for i in range(len(mat)):
            sums=0
            for j in range(len(mat[0])):
                sums+=mat[i][j]
            heapq.heappush(heapa,[sums,i])
        while k!=0:
            temp = heapq.heappop(heapa)
            res.append(temp[1])
            k=k-1
            
        return res
        
        
       
                