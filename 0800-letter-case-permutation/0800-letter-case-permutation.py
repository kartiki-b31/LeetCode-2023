class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        '''
        a1b2
        count_alpha=2
        
        recursive(str,idx):
        if len(res)==2**count_alpha
            res.append(str)
        if s[idx].isalpha():#a1b2
            recursive(str+s[idx].lower(),idx+1)
            
            recursive(str+s[idx].upper(),idx+1)
        else:
            recursive(str+s[idx],idx+1)

        '''
        def backtrack(cur,idx):
            if idx==len(s):
                res.append(cur)
                return
            
            if s[idx].isalpha():
                backtrack(cur+s[idx].lower(),idx+1)
                backtrack(cur+s[idx].upper(),idx+1)
            else:
                backtrack(cur+s[idx],idx+1)
        
        res=[]
        backtrack("",0)
        return res
