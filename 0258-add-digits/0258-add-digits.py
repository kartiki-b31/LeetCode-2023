class Solution:
    def addDigits(self, num: int) -> int:
        x=0
        y=0
        while(num>9):
            x=num%10
            y=num//10
            num=x+y
          
        
        return num