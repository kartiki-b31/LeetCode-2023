# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count=0
        if head==None:
            return None
        else:
            prev=None
            current=head
            while current!=None:
                prev=current
                count=count+1
                current=current.next

        if count%2==0:
            half=(count//2)+1
        else:
            half=(count//2)+1
        
        prev=None
        current=head
        i=0
        while i<half-1:
            prev=current
            current=current.next
            i=i+1
        return current