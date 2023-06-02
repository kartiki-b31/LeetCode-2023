class Solution:
    def addDigits(self, num: int) -> int:
        x=0
        y=0
        while(num>9):
            
            num=num%10 + num//10
          
        
        return num