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
def swapNodes(head, i, j) :
	#Your code goes here
    if(i>j):
        i=i+j
        j=i-j
        i=i-j
    
    # //Find nodes
    if(i==0):
        if(j==1):
            cur=head.next
            head.next=cur.next
            cur.next=head
            return cur
        
        pt=head
        prev = None
        for c in range(j):
            prev = pt
            pt=pt.next
        
        temp=head.next
        cur=pt.next
        
        head.next=cur
        pt.next=temp
        prev.next = head
        return pt
        
    
    if(j-i==1):
        pt=head
        prev = None
        for c in range(i):
            prev = pt
            pt=pt.next
        
        cur=pt.next
        cur1=cur.next
        prev.next = cur
        cur.next=pt
        pt.next=cur1
        # cur1.next=cur
        return head
        
    
    pt1=head
    pt2=head
    prevX= None
    prevY = None
    for c in range(i):
        prevX = pt1
        pt1=pt1.next
    
    for s in range(j):
        prevY = pt2
        pt2=pt2.next
    
    cur1=pt1.next
    cur2=pt2.next
    
    # temp=cur1.next
    
    # cur1.next=cur2.next
    # pt2.next=cur1
    # pt1.next=cur2
    # cur2.next=temp
    prevX .next = pt2
    pt2.next = cur1
    pt1.next = cur2
    prevY.next = pt1
    
    return head


        # return head

curr = swapNodes(head,3,5)
while curr is not None:
    print(curr.data,end  =" ")
    curr = curr.next
