class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        #[0,0,1,0,0]
        l=len(flowerbed)
        cnt=0
        for i in range(l):
            if flowerbed[i]==0:
                
                #left
                if i==0 or flowerbed[i-1]==0:
                    left=True
                else:
                    left=False
                #right
                if i==l-1 or flowerbed[i+1]==0:
                    right=True
                else:
                    right=False
            
            
            
                if left==True and right==True:
                    flowerbed[i]=1
                    cnt=cnt+1
                
        
        print(cnt)
        
        if n<=cnt:
            return True

                
                    
                
                
        