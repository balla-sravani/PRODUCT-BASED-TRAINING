class cse:
    x=10#static
    def __init__(self):
        self.y=30#non static
    def qwr(self):
        print("hi",a.y)
        print("hi",self.y)
a=cse()
a.qwr()
print(cse.x,a.y)
