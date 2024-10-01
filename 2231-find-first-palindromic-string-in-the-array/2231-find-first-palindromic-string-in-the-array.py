class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        #words.sort()
        print(words)
        def checkPlanidrome(s,i,j):
            while i<=j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
        
        res=False
        for w in words:
            res=checkPlanidrome(w,0,len(w)-1)
            if res==True:
                return w 


        return ""