class Node:
    value=None
    next=None
    def __init__(self, value, next):
        self.value=value
        self.next=next

def addNumbers(value, head):
    if(head==None):
        head=Node(value,None)
    else:
        prev=None
        current=head
        while(current!=None):
            prev=current
            current=current.next
        prev.next=Node(value, None)
    return head

def deletingNumber(head,x):
    if(head.value==x):
        temp=head.next
        del head
        return temp
    
    else:
        prev=None
        current=head
        while(current.value!=x):
            prev=current
            current=current.next
        prev.next=current.next
        del current
        return head

def addingNumberatIndex(value, head, i):
    if(i==0):
        head=Node(value,head)
    else:
        prev=None
        current=head
        for j in range(0,i):
            prev=current
            current=current.next
            if(current==None):
                break
        prev.next=Node(value, current)
    return head

def printingLinkedList(head):
    while(head!=None):
        print(head.value)
        head=head.next


# head=addNumbers(8,None)
# addNumbers(67,head)
# addNumbers(3,head)
# addNumbers(4,head)
# addNumbers(13,head)
# #deleteNumber(head,x)
# printingLinkedList(head)
# print('deleteing a number------------------')
# head=deletingNumber(head,8)
# printingLinkedList(head)


head=addNumbers(99,None)
addNumbers(67,head)
addNumbers(3,head)
addNumbers(4,head)
addNumbers(13,head)
printingLinkedList(head)
print("adding at index-------------")
head=addingNumberatIndex(100,head,10)
printingLinkedList(head)
