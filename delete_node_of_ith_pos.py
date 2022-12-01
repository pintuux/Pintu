class node:
    def __init__(self,data):
        self.data = data
        self.next = None
def delete_ith_pos_node(head, pos) :
    # Write your code here.
    prev = head
    temp1 = head
    count = 0
    while temp1 is not None:
        if  pos == 0:
            head = temp1.next
            temp1.next = None
            # free(temp1)
            return head
        elif count == pos:
            prev.next = temp1.next
            temp1.next = None
            return head
        else:
            count += 1
            prev = temp1
            temp1 = temp1.next 
    else:
        return head
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
i = int(input("Enter which position node element you want to delete"))
curr1 = delete_ith_pos_node(curr,i)
while curr1 is not None:
    print(curr1.data,end =" ")
    curr1 = curr1.next

