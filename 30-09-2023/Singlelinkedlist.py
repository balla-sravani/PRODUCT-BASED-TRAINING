class node:
    def __init__(self,z):
        self.data=z
        self.next=None
class cse:
    def __init__(self):
        self.head=None
    def cre(self,x):
        if(self.head==None):
            self.head=node(x)
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=node(x)
    def display(self):
        temp=self.head
        while(temp!=None):
            print(temp.data,end="->")
            temp=temp.next
    def addnodefront(self,x):
        if(self.head==None):
            self.head=node(x)
        else:
            temp=node(x)
            temp.next=self.head
            self.head=temp
b=cse()
c=cse()
b.cre(10)
b.cre(20)
b.cre(30)
b.addnodefront(200)
c.cre(20)
c.cre(40)
c.display()
print()
b.display()
    
