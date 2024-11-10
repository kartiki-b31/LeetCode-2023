# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        '''
        d={0:5,1:4,2:3,3:1,}
        n=8
        sum(0,7)+1==8,twin

        0 1 2 3   4 5 6 7 
        5 4 3 1 | 2 4 2 1 
              
        '''
        current=head
        count=1
        d={}
        while current.next!=None:
            count+=1
            current=current.next

        current=head

        i=0
        maxi_val=0
        while current!=None:
            d[i]=current.val
            #i+x+1=count
            #x=count-i-1
            #print(current.val)
            if count-i-1 in d:
                maxi=d[i]+d[count-i-1]
                maxi_val=max(maxi,maxi_val)
            i+=1
            current=current.next


        return maxi_val

    