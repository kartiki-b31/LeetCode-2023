class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        count=0;
        current=[]
        for i in range(len(nums)):
            if nums[i]!=0:
                current=nums[i]
                count+=1
                for j in range(i+1,len(nums)):
                    nums[j]-=current
                    
                    
        return count

         
            
                
        