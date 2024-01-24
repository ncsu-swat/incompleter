#Source: https://stackoverflow.com/questions/50007708/nameerror-name-mergelist-is-not-defined
class node:
    def __init__(self, data):
        self.data=data
        self.head=None
class linkedlist:
    def __init__(self):
        self.head=None
    def push(self, newdata):   
        newnode=node(newdata)
        newnode.next=self.head
        self.head=newnode
    def mergelist(self, l1, l2):
        dummy=listnode(0)
        pointer=dummy
        while(l1 and l2):
            if l1.data<=l2.data:
                pointer.next=l1
                l1=l1.next
            else:
                pointer.next=l2
                l2=l2.next
            pointer=pointer.next
        if l1 == None:
            pointer.next = l2
        else:
            pointer.next = l1
        return dummy.next   
    def printlist(self):
        temp=self.head
        while(temp):    

            print(temp.data)
            temp=temp.next            
llist1=linkedlist()
llist1.push(4)  
llist1.push(9)    
llist1.push(7)    
llist1.push(5)    
llist1.push(4)   

llist2=linkedlist() 
llist2.push(32)  
llist2.push(12)
llist2.push(1)
llist2.push(2)
llist2.push(8)
llist1.printlist()
llist2.printlist() 

llist3=linkedlist()
llist3.head=mergelist(llist1.head, llist2.head)

llist3.printlist()