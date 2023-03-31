class Solution(object):
    def removeVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel=['a','e','i','o','u']
        result=""
        
        for c in s:
            if c in vowel:
                continue
        
            result=result+c
        
        
        return result