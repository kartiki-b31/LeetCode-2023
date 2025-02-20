class Solution:
    def balancedStringSplit(self, s: str) -> int:
        n=len(s)
        left=0
        right=0
        max_len=0
        for si in s:
            if si=="L":
                left+=1
            else:
                right+=1
            if left==right:
                max_len+=1
        
        return max_len
