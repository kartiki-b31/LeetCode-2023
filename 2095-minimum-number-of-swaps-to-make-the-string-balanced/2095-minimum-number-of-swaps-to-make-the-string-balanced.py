class Solution:
    def minSwaps(self, s: str) -> int:
        mismatches=0
        for c in s:
            if c=="]" and mismatches!=0:
                mismatches-=1
            elif c=="[":
                mismatches+=1
        
        return math.ceil(mismatches/2)