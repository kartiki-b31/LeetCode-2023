class Solution:
    def convert(self, s: str, numRows: int) -> str:
        currow=0
        step=1
        list=['']*numRows
        if numRows==1:
            return s
        
        for i in s:
            list[currow]+=i
            if currow==numRows-1:
                step=-1
            elif currow==0:
                step=1
            currow+=step
        
        res=""
        for i in range(len(list)):
            res+=list[i]
        
        return res
            