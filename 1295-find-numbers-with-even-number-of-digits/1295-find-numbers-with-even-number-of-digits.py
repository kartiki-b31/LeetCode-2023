class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        str1=""
        count=0
        for i in range(len(nums)):
            str1=str(nums[i])
            if len(str1)%2==0:
                count=count+1
            #print(str1)
            
        return count