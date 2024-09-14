```python
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

head=Node(2)
tow=Node(4)
head.next=tow
three=Node(9)
tow.next=three

while(head):
    print(head.data)
    head=head.next
print(head)
```

## build Linklist 

Creating linklist till -1

```python
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
```
