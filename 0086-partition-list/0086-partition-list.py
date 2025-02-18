# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None): #integre, pointer
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head==None:
            return None

        nums=[]
        while head:
            nums.append(head.val)
            head=head.next
        print(nums)
        small_val=[]
        great_val=[]
        for i in range(len(nums)):
            if nums[i]<x:
                small_val.append(nums[i])
            else:
                great_val.append(nums[i])
        ans=small_val+great_val
        temphead=ListNode()
        curr=temphead
        for i in ans:
            temp=ListNode()
            temp.val=i
            curr.next=temp
            curr=curr.next
            
        return temphead.next