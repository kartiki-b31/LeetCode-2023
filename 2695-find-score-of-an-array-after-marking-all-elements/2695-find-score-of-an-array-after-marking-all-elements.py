class Solution:
    def findScore(self, nums: List[int]) -> int:
        n=len(nums)
        visited=set()
        heap=[]
        j=0
        score=0
        for i in range(n):
            heap.append((nums[i],i))
        heapq.heapify(heap)
        
        while len(visited)<n:
            (mini_val,idx)=heappop(heap)
            if (mini_val,idx) not in visited:
                visited.add((mini_val,idx))
                score+=mini_val
                if idx-1!=-1:
                    visited.add((nums[idx-1],idx-1))
                if idx+1!=n:
                    visited.add((nums[idx+1],idx+1))

            #print(len(visited))
            #print("score",score)

            
        return score

