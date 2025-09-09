
class Student:

    def __init__(self, Id=0, Name="UnKnown", Age=0, Grade="UnKnown"):
        self.Id = Id
        self.Name = Name
        self.Age = Age
        self.Grade = Grade


s1 = Student()
s2 = Student(1, "Barane", 21, "B")

print(s1.__dict__)
print(s2.__dict__)
