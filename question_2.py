"""
Create a Python class Person with attributes: name and age of type string.
Create a display() method that displays the name and age of an object created via the Person class.
Create a child class Student  which inherits from the Person class and which also has a section attribute.
Create a method displayStudent() that displays the name, age and section of an object created via the Student class.
Create a student object via an instantiation on the Student class and then test the displayStudent method.
"""
class Person:
    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
    
    def display(self) -> None:
        """
        This function displays the name and age of the stored in Person Class.
        """
        print(f"[INFO] <Name>: {self.name}", end=" ")
        print(f"<Age>: {self.age}")
    

class Student(Person):
    def __init__(self, name: str, age: str, section: str) -> None:
        super().__init__(name, age)
        self.section = section
    
    def display_student(self) -> None:
        super().display()
        print(f"[INFO] <Section>: {self.section}")

std_1 = Student("Talha", "22", "A")
std_2 = Student("Hamza", "24", "A")
std_1.display_student()
std_2.display_student()
