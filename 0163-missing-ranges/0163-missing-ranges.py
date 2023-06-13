class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        n=len(nums)
        answer=[]
        if n==0:
            answer.append([lower,upper])
            return answer
        if lower < nums[0]:
            answer.append([lower,nums[0]-1])
            
        for i in range(n-1):
            if nums[i+1] -nums[i]<=1:
                continue
            answer.append([nums[i]+1,nums[i+1]-1])
            
        if upper > nums[n-1]:
            answer.append([nums[n-1]+1,upper])
            
        return answer