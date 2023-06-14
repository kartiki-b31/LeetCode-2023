class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        c=Counter(nums)
        #print(c)
        n=len(nums)
        #print(n)
        # sum=0
        # sum2=0
        # sum2=n*(n-1)
        for i in range(n+1):
            if i not in c:
                return i   
            
            
        