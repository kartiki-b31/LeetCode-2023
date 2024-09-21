class Solution:
    def shortestPalindrome(self, s: str) -> str:
        len_s=len(s) #"aacecaaa" len=8
        reversed_str=s[::-1] #"aaacecaa"
        for i in range(len_s): #i=1
            if s[:len_s-i]==reversed_str[i:]: #aacecaa==aacecaa
                return reversed_str[:i]+s #a+aacecaaa
        return ""