# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return None
        else:
            prevNode=None
            currentNode=head
            NextNode=head.next
            while(currentNode!=None):
                currentNode.next=prevNode
                prevNode=currentNode
                currentNode=NextNode
                if NextNode!=None:
                    NextNode=NextNode.next
            return prevNode
                
        