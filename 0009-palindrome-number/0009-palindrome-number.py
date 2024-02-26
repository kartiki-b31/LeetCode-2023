class Solution:
    def isPalindrome(self, x: int) -> bool:
        stringg=str(x)
        n=len(stringg)
        list=[]
        list[:]=stringg
        for i in range(len(list)):
            if list[i]!=list[n-1-i]:
                
                return False
            
        return True
                
        