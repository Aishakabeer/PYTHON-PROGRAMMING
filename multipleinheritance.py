class parent():
    def func1(self):
        print("This is first function")
class parent2():
    def func2(self):
        print("This is seconed function")
class child(parent,parent2):
    def func3(self):
        print("This is the third function")
obj1=child()
obj1.func1()
obj1.func2()
obj1.func3()
