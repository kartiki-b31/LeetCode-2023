# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        prev=None
        current=head
        nums=[]
        while(current!=None):
            prev=current
            nums.append(current.val)
            current=current.next
            
        n=len(nums)
        sums=[]
        for i in range(len(nums)):
            j=n-1-i
            sums.append(nums[i]+nums[j])
    
        maximum=0
        for i in range(len(sums)):
            if sums[i]>maximum:
                maximum=sums[i]
        return maximum
        
            
        