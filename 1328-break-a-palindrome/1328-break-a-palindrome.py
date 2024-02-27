class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n=len(palindrome)
        palindromelist=[]
        palindromelist[:]=palindrome
        if len(palindromelist)==1:
                return ""
        for i in range(len(palindromelist)//2):
            
            if palindromelist[i]!='a':
                palindromelist[i]='a'
                return "".join(palindromelist)
                
        #if palindromelist[n-1]=='a':
        palindromelist[n-1]='b'
            
        return "".join(palindromelist)