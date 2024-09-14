class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def buildLinkList():
    head=None
    tail=head
    while(True):
        data=int(input())
        if(data==-1):
            return head
        newN=Node(data)
        if(head==None):
            head=newN
            tail=newN
        else:
            tail.next=newN
            tail=newN
    

head=buildLinkList()
while(head):
    print(head.data,end="->")
    head=head.next
print(head)