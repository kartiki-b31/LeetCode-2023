class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        strli=list(strs)
        n=len(strs)
        start=strli[0]
        end=strli[n-1]

        result=[]
        for i in range(len(start)):
            if start[i]!=end[i]:
                break
            else:
                result.append(start[i])
        return "".join(result)