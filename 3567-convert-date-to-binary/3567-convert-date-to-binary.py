class Solution:
    def convertDateToBinary(self, date: str) -> str:
        y,m,d=date.split("-")
        
        y=str(bin(int(y)))
        y=y.replace("0b","")
        
        m=str(bin(int(m)))
        m=m.replace("0b","")
        
        d=str(bin(int(d)))
        d=d.replace("0b","")
        
        res=""
        res=y+"-"+m+"-"+d



        return res