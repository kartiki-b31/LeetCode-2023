class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        #[5,8,6]
        #k=3
        #5,5,3,5,1
        #k=11, 2,2,3
        def isValid(mid):
            n=len(candies)
            total=0
            for c in candies:
                total+=(c//mid)
                if total>=k:
                    return True
            return False

        start=1
        end=sum(candies)//k
        candies.sort()
        #[5,6,8]
        while start<=end:
            mid=(start+end)//2
            if isValid(mid):
                start=mid+1
            else:
                end=mid-1
        return end