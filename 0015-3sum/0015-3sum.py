class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            low=i+1
            high=len(nums)-1

            while low<high:
                total=nums[i]+nums[low]+nums[high]
                if total>0:
                    high-=1
                elif total<0:
                    low+=1
                else:
                    res.append([nums[i],nums[low],nums[high]])
                    low+=1
                    while nums[low]==nums[low-1] and low<high:
                        low+=1
        return res
