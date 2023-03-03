# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00

    def __init__(self, name: str, color: str, kind: str, value: float) -> None:
        self.name = name
        self.color = color
        self.value = value
        self.kind = kind
        
    def description(self) -> None:
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here

car1 = Vehicle("Fer", "red", "convertible", 60000)
car2 = Vehicle("jump", "blue", "van", 10000)
# test code
print(car1.description())
print(car2.description())