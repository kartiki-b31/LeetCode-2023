class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        diction={}
        for i,v in enumerate(order):
            diction[v]=i
        arr=[]
        
        for j in range(len(words[0])):
            
            arr.append(diction[words[0][j]])
        
        
        for i in range(1,len(words)):
            arr2=[]
            for j in range(len(words[i])):
                arr2.append(diction[words[i][j]])
            print(arr2)
            
            if arr > arr2:
                return False
            
            arr=arr2
        
            
        return True
        
            