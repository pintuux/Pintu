class node:
    def __init__(self,data):
        self.data = data
        self.next = None
def insert_at_ith_positon(curr,i,x):
    l = length(curr)
    if i < 0 and i> l:
        return curr
    else:
        prev = None
        current = curr
        for j in range(i):
            prev = current
            current = current.next
        node1 = node(x)
        prev.next = node1
        node1.next = current
    return curr
            
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
i = int(input("Enter the position where you want to add a node"))
x = int(input())
temp = insert_at_ith_positon(curr, i, x)
while temp is not None:
    print(temp.data, end =" ")
    temp = temp.next
# while curr is not None:
#     print(curr.data)
#     curr = curr.next



