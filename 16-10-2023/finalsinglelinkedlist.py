class node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def insertatbeg(self,data):
        if self.head==None:
            self .head=node(data)
        else:
            temp=node(data)
            temp.next=self.head
            self.head=temp
    def  display(self):
        temp=self.head
        while(temp!=None):
            print(temp.val,end="->")
            temp=temp.next
    def insertlast(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=node(data)
    def deletebeg(self):
        if self.head==None:
            return
        temp=self.head
        self.head=self.head.next
        temp.next=None
        return temp.val
    def deleteend(self):
        if self.head==None:
            return
        temp=self.head
        while(temp.next.next):
            temp=temp.next
            new=temp.next.val
        temp.next=None
        return new
        
        
        
        
                
                
l=[2,4,6,8,9]
o=sll()
for i in l:
    o.insertlast(i)
'''
for i in l:
    o.insertatbeg(i)'''
o.display()
print()
print(o.deleteend())
o.display()
print()
print(o.deletebeg())
o.display()