from abc import ABC , abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius * self.radius
    
c = Circle(5)
# s = Shape()
# print(f"Area of the circle: {c.area()}")


class Person(ABC):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_role(self):
        return f"Person {self.name} {self.surname}"

    @abstractmethod
    def get_details(self):
        pass
    
    # @abstractmethod
    def speak(self):
        # print(f"{self.name} {self.surname} is speaking")
        return f"Student {self.name} {self.surname} is speaking"

class Student(Person):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_details(self):
        return f"Student Name: {self.name}, Surname: {self.surname}"

# e = Person()
emp = Student("Alice", "Smith")
print(emp.get_details())
print(emp.get_role())
print(emp.speak())