# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len_ll=1
        if head==None:
            return None
        
        temp=head
        while temp.next!=None:
            len_ll+=1
            temp=temp.next
        
        idx=len_ll-n
        if idx==0:
            temp=head.next
            del head
            return temp
        else:
            prev=None
            current=head
            for j in range(0,idx):
                prev=current
                current=current.next
            prev.next=current.next
            del current
            return head



        
