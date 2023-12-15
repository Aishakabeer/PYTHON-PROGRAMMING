class parent():
    def func1(self):
        print("This is the first function")
class child(parent):
        def func2(self):
            print("This is the second function")
class child2(child):
        def func3(self):
            print("This is the third function")
obj1 = child2()
obj1.func1()
obj1.func2()
obj1.func3()
    
