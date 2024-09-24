class Solution:
    def frequencySort(self, s: str) -> str:
        freq={}
        for c in s:
            freq[c]=1+freq.get(c,0)
        
        freq=sorted(freq.items(),key=lambda x: -x[1])

        print(freq)
        ans=""
        for k,v in freq:
            ans+=k*v
        return ans
