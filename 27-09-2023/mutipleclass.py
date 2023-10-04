class Siva:
    def gold(self):
        print ("hello")
    def car(self):
        print("hi")
class Baby1(Siva):
    def method1(self):
        print("how")
class Baby2(Siva):
    def method2(self):
        print ("you")
obj=Baby1()
obj.method1()
obj.car()
obj.gold()
obj1=Baby2()
obj1.method2()
obj1.car()
obj1.gold()
