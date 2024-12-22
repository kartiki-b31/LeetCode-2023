class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split(" ")
        #print(s)
        ans=[]
        final_ans=[]
        for chunk in s:
            rev=[]
            for i in range(len(chunk)-1,-1,-1):
                rev.append(chunk[i])
            ans.append(rev)
        
        for arr in ans:
            final_ans.append((" ")+("".join(arr)))
        
       # print(final_ans[0])
        final_ans[0]=final_ans[0].replace(" ","")
        #print(final_ans[0])

        return "".join(final_ans)