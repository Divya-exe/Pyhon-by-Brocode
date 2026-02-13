class Student:
    def __init__(self, name, gpa):
        self.name=name
        self.gpa=gpa
    
    def __str__(self):
        return f"name= {self.name}, gpa={self.gpa}"
    
    def __eq__(self,other):
        return self.name==other.name
        
    def __gt__(self,other):
        return self.gpa>other.gpa
    
student1= Student("Divya",3.2)
student2= Student("Rushi",2.5)
    
print(student1)
print(student2)
print(student1==student2)
print(student1>student2)