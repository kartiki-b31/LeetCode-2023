class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        countSum=nums[0]
        for i in range(1,len(nums)):
            if (nums[i]-nums[i-1])==1:
                countSum+=nums[i]
            else:
                break
        #print(countSum)
        nums.sort()
        for i in range(len(nums)):
            if countSum==nums[i]:
                countSum+=1
        return countSum