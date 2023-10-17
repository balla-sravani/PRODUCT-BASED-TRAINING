class node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def insertatbeg(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            temp=node(data)
            temp.next=self.head
            self.head.prev=temp
            self.head=temp
    def  display(self):
        temp=self.head
        while(temp!=None):
            print(temp.val,end="->")
            temp=temp.next
    def insertlast(self,data):
        if self.head==None:
            self.head=node(data)
            tail.head=self.head
        else:
            temp=node(data)
            temp.prev=self.tail
            self.tail.next=new
            self.tail=new
            
    def deletebeg(self):
        if self.head==None:
            return
        self.head=self.head.next
        self.head.prev=None
    def deleteend(self):
        if self.head==None:
            return
        #self.tail=self.tail.prev
        #self.tail.next=None
        self.tail.prev.next=None
        
        
        
        
                
                
l=[2,4,6,8,9]
o=dll()
'''for i in l:
    o.insertlast(i)
'''
for i in l:
    o.insertatbeg(i)
o.display()
print()
o.deleteend()
o.display()
print()
o.deletebeg()
o.display()

