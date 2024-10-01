class Solution:
    def largestPalindromic(self, num: str) -> str:
        count=Counter(num)
        print(count)
        palin=mid=''
        for i in sorted(count.keys(),reverse=True):
            mid=max(mid,i*(count[i] & 1))
            palin+=i*(count[i]//2)
        palin=palin.lstrip('0')
        return (palin +mid+palin[::-1]) or '0'