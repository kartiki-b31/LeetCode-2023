class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s=s.replace(" ","")
        s=s.replace(":","")
        s=s.replace(";","")
        s=s.replace(",","")
        s=s.replace(".","")
        s=s.replace("@","")
        s=s.replace("#","")
        s=s.replace("_","")
        print(s)
        i=0
        n=len(s)-1
        j=n
        while i<=j:
            if s[i]!=s[j]:
                return False
            
            i+=1
            j-=1
        return True