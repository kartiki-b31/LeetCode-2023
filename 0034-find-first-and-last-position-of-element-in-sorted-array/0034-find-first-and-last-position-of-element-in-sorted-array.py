class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res_arr=[]

        start=0
        end=len(nums)-1
        fi=-1
        while start<=end:
            mid=(start+end)//2
            if nums[mid]==target:
                fi=mid
                end=mid-1
            elif nums[mid]>target:
                end=mid-1
            else:
                start=mid+1
        start=0
        end=len(nums)-1
        ei=-1
        while start<=end:
            mid=(start+end)//2
            if nums[mid]==target:
                ei=mid
                start=mid+1
            elif nums[mid]>target:
                end=mid-1
            else:
                start=mid+1
        return [fi,ei]