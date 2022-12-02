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
head = takeinput()
def printReverse(head) :
    # #Your code goes here
    # while head is not None:
    #         print(head.data,end =" ")
    #         head = head.next
    if head == None or head.next is None:
        return head
    # if head.next is None:
    #     # print(head.data)
    #     return head
    else:
        forword = None
        prev = None
        temp = head
        while temp is not None:
            forword = temp.next
            temp.next = prev
            prev = temp
            temp = forword
        return prev
curr = printReverse(head)
while curr is not None:
    print(curr.data,end = " ")
    curr = curr.next