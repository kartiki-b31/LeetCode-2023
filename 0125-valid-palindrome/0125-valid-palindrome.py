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
        for char in s:
            if char.isalnum():
                new_str=new_str+char

        print(s)
        i=0
        n=len(new_str)-1
        j=n
        while i<=j:
            if new_str[i]!=new_str[j]:
                return False
            
            i+=1
            j-=1
        return True