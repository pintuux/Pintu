class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def create_linked_list():
    inputElement = [int(i) for i in input().split()]
    head = None

    for i in inputElement:
        node = Node(i)
        if head is None:
            head = node
            curr = head
        else:
            curr.next = node
            curr = curr.next
    return head
head = create_linked_list()
head2 = head
def printReverse(head) :
    if head == None or head.next is None:
        return head
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
def palindrome(curr,head2):
        
    while head2 is not None and curr is not None:
        if head2.data == curr.data:
            head2 = head2.next
            curr = curr.next
        else:
            return False
    else:
        return True
check = palindrome(curr,head2)
if check:
    print("ture")
else:
    print("false")
