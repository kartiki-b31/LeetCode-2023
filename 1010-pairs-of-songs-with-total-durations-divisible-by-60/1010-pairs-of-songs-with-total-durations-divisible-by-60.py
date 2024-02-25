class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ans=0
        rem=collections.defaultdict(int)
        n=0
        for t in time:
            if t%60==0:
                ans+=rem[0]
            else:
                ans+=rem[60-t%60]
            rem[t%60]+=1
        return ans