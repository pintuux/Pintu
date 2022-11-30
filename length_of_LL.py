class node :
    def __init__(self, data) :
        self.data = data
        self.next = None
def length(head) :
    #Your code goes here
    temp = head
    count = 0
    while temp is not None:
        count += 1
        temp = temp.next
    return count
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
print(length(curr))