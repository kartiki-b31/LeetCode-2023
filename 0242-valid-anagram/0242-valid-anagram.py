class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
#         if len(s)==len(t):
#             if sorted(s)==sorted(t):
#                 return True
#         else:
#             return False
        
        if len(s)==len(t):
            if Counter(s)==Counter(t):
                return True
        
        else:
            return False