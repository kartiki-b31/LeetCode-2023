class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPlanidrome(s,i,j):
            while i<j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
        

        i=0
        j=len(s)-1
        while i<j: #baac #baa or aac
            if s[i]!=s[j]:
                return checkPlanidrome(s,i,j-1) or checkPlanidrome(s,i+1,j)
            i += 1
            j -= 1
        
        return True