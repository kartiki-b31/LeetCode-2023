# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current1=list1
        current2=list2
        temp1=None
        temp2=None
        head = None
        current = None
        while(True):
            if current1==None or current2==None:
                break
            value = None
            if current1.val >= current2.val:
                value = current2.val
                current2 = current2.next
            else:
                value = current1.val
                current1 = current1.next
            
            
            if head == None:
                head = ListNode(value, None)
                current = head
            else:
                current.next = ListNode(value, None)
                current = current.next
        
        while(current1!=None):
            if head == None:
                head = ListNode(current1.val, None)
                current = head
            else:
                current.next = ListNode(current1.val, None)
                current = current.next
            current1 = current1.next
            
        while(current2!=None):
            if head == None:
                head = ListNode(current2.val, None)
                current = head
            else:
                current.next = ListNode(current2.val, None)
                current = current.next
            current2 = current2.next
            
        return head
            

                
                
        