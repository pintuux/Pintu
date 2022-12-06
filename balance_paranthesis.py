def isBalanced(expression) :
    l = []
    for i in expression:
        if i in '({[':
           l.append(i)
        #    top= i
        elif i == ')':
            if (not l) or l[-1] != '(':
                return False
            else:
                l.pop()
        elif i == '}':
            if (not l) or l[-1] != '{':
                return False
            else:
                l.pop()
        elif i == ']':
            if (not l) or l[-1] != '[':
                return False
            else:
                l.pop()
             
    if len(l)==0:
        return True
    else:
        return False            	
s = input("enter paranthesis")
if isBalanced(s):
    print("true")
else:
    print("false")

