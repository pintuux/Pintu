class node:
    def __init__(self,data):
        self.data = data
        self.next = None
def takeinput():
        
    inputnode = [int(i) for i in input().split()]
    head = None
    for i in inputnode:
        node1 = node(i)
        if head is None:
            head = node1
            curr = head
        else:
            curr.next = node1
            curr = node1
    return head
curr = takeinput()

while curr is not None:
    print(curr.data)
    curr = curr.next


