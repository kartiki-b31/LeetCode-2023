class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows==1:
            return [[1]]
        if numRows==2:
            return [[1],[1,1]]
        results=[]
        prev=[1,1]
        ans=[[1],[1,1]]
        
        for i in range(3,numRows+1):
            results.append(1)
            for j in range(1,len(prev)):
                results.append(prev[j-1]+prev[j])
            results.append(1)
            ans.append(results)
            prev=results
            results=[]
        
        return ans
            
                