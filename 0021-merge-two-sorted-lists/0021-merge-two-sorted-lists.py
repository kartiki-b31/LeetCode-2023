# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        head=None
        while(list1 and list2):
            if list1.val > list2.val:
                if head == None:
                    head = ListNode(list2.val, None)
                    
                else:
                    current = head
                    while(current.next!=None):
                        
                        current = current.next
                    current.next = ListNode(list2.val, None)
                    
                list2=list2.next
                
            else:
                if head == None:
                    head = ListNode(list1.val, None)
                    
                else:
                    current = head
                    while(current.next!=None):
                        
                        current = current.next
                    current.next = ListNode(list1.val, None)
                    
                list1=list1.next
                    
            
        while(list1):
            if head == None:
                head = ListNode(list1.val, None)
                
            else:
                current = head
                while(current.next!=None):
                    current = current.next
                current.next = ListNode(list1.val, None)
            list1=list1.next
                    
        while(list2):
            if head == None:
                head = ListNode(list2.val, None)
                
            else:
                current = head
                while(current.next!=None):
                    current = current.next
                current.next = ListNode(list2.val, None)
            list2=list2.next
            
        return head
            

                
                
        