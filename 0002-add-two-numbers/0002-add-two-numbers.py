# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result=ListNode(0)
        ptr=result
        carry=0
        while(l1!=None or l2!=None or carry!=0):
            sum=0+carry
            
            if l1!=None:
                sum=sum+l1.val
                l1=l1.next
            if l2!=None:
                sum=sum+l2.val
                l2=l2.next
            
            carry=sum//10
            print(carry)
            sum=sum%10
            newNode=ListNode(sum)
            ptr.next=newNode
            ptr=newNode
            
            
        #if carry==1:
         #   result.next=ListNode(1)
            #result=result.next
        return result.next
        
        