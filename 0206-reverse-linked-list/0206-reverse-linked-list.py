# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head==None):
            return None
        else:
            previousNode=None
            currentNode=head
            nextNode=head.next
            while(nextNode!=None):
                currentNode.next=previousNode
                previousNode=currentNode
                currentNode=nextNode
                nextNode=nextNode.next
            currentNode.next=previousNode  
            return currentNode
                
        