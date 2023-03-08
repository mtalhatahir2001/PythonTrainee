class Person:
    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
    
    def display(self) -> None:
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
