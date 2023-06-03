# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
   
 
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if(head==None):
            return True
        
        slow=self.end_of_first_half(head)
        rev=self.reversingLinkedList(slow)

        return self.palindrome_exists(head,rev)
        
    def end_of_first_half(self,head):
        fast=head
        slow=head
        while fast.next is not None and fast.next.next is not None:
            fast=fast.next.next
            slow=slow.next
        return slow
    
    def reversingLinkedList(self,head):
        if(head==None):
            return None
    
        previousNode=None
        currentNode=head
        NextNode=head.next

        while(NextNode!=None):
            currentNode.next=previousNode
            previousNode=currentNode
            currentNode=NextNode
            NextNode=NextNode.next
        currentNode.next=previousNode
        return currentNode  
    
    def palindrome_exists(self,head,rev):

        result=True
        while head and rev is not None:
            if head.val!=rev.val:
                result=False
        
            head=head.next
            rev=rev.next
        return result

    
        