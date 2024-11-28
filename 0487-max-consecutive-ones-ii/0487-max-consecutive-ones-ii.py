class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n=len(nums)
        left=0
        right=0
        longest_seq=0
        numZeroes=0
        for right in range(n):
            if nums[right]==0:
                numZeroes+=1
                while numZeroes==2:
                    if nums[left]==0:
                        numZeroes-=1
                    left+=1
            longest_seq=max(longest_seq,right-left+1)


        return longest_seq