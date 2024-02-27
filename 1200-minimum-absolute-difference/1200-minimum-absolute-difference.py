class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res=[]
        mini=float('inf')
       
        for i in range(1,len(arr)):
            mini=min(arr[i]-arr[i-1],mini)
            
            
        for i in range(len(arr)):
            if (arr[i]-arr[i-1])==mini:
                res.append([arr[i-1],arr[i]])
                
        return res
                
            
        