## __str__ controlls what should be returned when the class is represented as a string.
## The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"My name is {self.name} and my age is {self.age}."
    def get_age(self):
        return f"My age is {self.age}."
    
p1 = Person('Asrar',21)
print(p1)

print(p1.get_age())