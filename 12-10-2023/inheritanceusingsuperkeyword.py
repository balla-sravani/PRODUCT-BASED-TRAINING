class cse:
    def fun1(self):
        print("sr")
class two:
    def fun2(self):
        print("university")
class three(cse,two):
    def fun3(self):
        print("hello")
        super().fun1()
o=three()
o.fun3()
o.fun1()
o.fun2()
        