class Person(object):
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
    def display(self):
        print(self.name,self.rollno)
emp = Person("Aisha",24)
emp.display()
class emp(Person):
    def show(self):
        print("Emp Class called")
emp_details = emp("Sumina",102)
emp_details.display()
emp_details.show()



        
