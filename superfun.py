class person:
    def __init__(self, name,age):
        self.name = name
        self.age = age
        
    def display(self):
        print("Name : ",self.name,"\nAge : ",self.age)
        
class employee(person):
    def __init__(self, name, age,empno,address):
        super().__init__(name, age)
        self.empno=empno
        self.address=address
        
    def display(self):
        super().display()
        print("empno",self.empno)
        print("Address",self.address)
e1 = employee("aish", 21, "001","ktm")
e1.display()

        
