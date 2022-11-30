
class node :
    def __init__(self, data) :
        self.data = data
        self.next = None
def printIthNode(head, i):
    #Your code goes here
    temp = head
    count = 0
    while temp is not None:
        count += 1
        temp = temp.next
    # print(count)
    temp = head
    if i < count:
        for j in range(i):
            
            # print(temp.data,end = " ")
            temp = temp.next
        print( temp.data)
    else:
        return -1
def takeinput():
        
    
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
inputnode = [int(i) for i in input().split()]
i = int(input("Enter value of i which you want to print"))
curr = takeinput()
printIthNode(curr,i)
