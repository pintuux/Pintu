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
head1 = takeinput()
head2 = takeinput()
def mergeTwoSortedLinkedLists(head1, head2):

    # Write your code hereh
    if head1 is None and head2 is None:
        return 
    if head1 is None and head2 is not None:
        return head2
    if head1 is not None and head2 is None:
        return head1

    fh = None
    ft = None
    if head1.data > head2.data:
        fh = head2
        ft = head2
        head2 = head2.next
    else:
        fh = head1
        ft = head1
        head1 = head1.next
    while head1 is not None and head2 is not None:
        if head1.data > head2.data:
            ft.next = head2
            ft = head2
            head2 = head2.next
        else:
            ft.next = head1
            ft = head1
            head1 = head1.next
    while head1 is not None:
        ft.next = head1
        ft = head1
        head1 = head1.next
    while head2 is not None:
        ft.next = head2
        ft = head2
        head2 = head2.next
    return fh
lis = mergeTwoSortedLinkedLists(head1, head2)
while lis is not None:
    print(lis.data,end = " ")
    lis = lis.next
