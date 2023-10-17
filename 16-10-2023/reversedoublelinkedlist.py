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
            self.tail=temp
    def reverse(self):
        curr=self.head
        while curr:
            curr.prev,curr.next=curr.next,curr.prev
            curr=curr.prev
            self.head,self.tail=self.tail,self.head
    
        
        
        
        
                
                
l=[2,4,6,8,9]
o=dll()
'''for i in l:
    o.insertlast(i)
'''
for i in l:
    o.insertatbeg(i)
o.display()
print()
o.reverse()
o.display()


