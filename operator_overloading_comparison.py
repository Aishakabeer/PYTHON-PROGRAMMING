class A:
 def __init__(self, a):
    self.a =a
 def __gt__(self,other):
     if(self.a>other.a):
         return True
     else:
        return False
obj1=A(1)
obj2=A(3)
if(obj1>obj2):
     print("object 2 is greater than object 1")
else:
     print("object 1 is greater than object 2")
        
