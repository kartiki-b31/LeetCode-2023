# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l2
        ret = ans = ListNode(-1)
        carry = 0
        while l1 and l2:
            ss = l1.val + l2.val + carry
            carry = ss // 10
            ss = ss % 10
            node = ListNode(ss)
            ans.next = node
            ans = ans.next
            l1, l2 = l1.next, l2.next
        while l1:
            ss = l1.val + carry
            carry = ss // 10
            ss = ss % 10
            node = ListNode(ss)
            ans.next = node
            ans = ans.next
            l1 = l1.next
        while l2:
            ss = l2.val + carry
            carry = ss // 10
            ss = ss % 10
            node = ListNode(ss)
            ans.next = node
            ans = ans.next
            l2 = l2.next
        if carry:
            ans.next = ListNode(1)
        return ret.next
        