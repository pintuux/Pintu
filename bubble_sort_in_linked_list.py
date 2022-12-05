def  number_of_node(head):
    count = 0
    temp = head
    while temp is not None:
        count += 1
        temp = temp.next
    return count
def bubbleSort(head) :
	#Your code goes here
    count = number_of_node(head)
    for i in range(count -1 ):
        temp = head
        for j in range(count -1 -i):
            if temp.data < temp.next.data:
                temp = temp.next
            else:
                pre = temp.data
                temp.data = temp.next.data
                temp.next.data = pre
                temp = temp.next
    return head