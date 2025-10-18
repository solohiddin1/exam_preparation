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






# class Person(ABC):
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname

#     def get_role(self):
#         return f"Person {self.name} {self.surname}"

#     # @abstractmethod
#     def get_details(self):
#         pass
    
#     # @abstractmethod
#     def speak(self):
#         # print(f"{self.name} {self.surname} is speaking")
#         return f"Student {self.name} {self.surname} is speaking"

# class Student(Person):
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname

#     def get_details(self):
#         # print(f"{self.speak()}")
#         return f"Student Name: {self.name}, Surname: {self.surname} is studying."
    
#     @abstractmethod
#     def speak(self):
#         return f"Student {self.name} {self.surname} says hello!"

# e = Person()
# st = Student("Alice", "Smith")
# print(st.get_details())
# print(st.get_role())
# print(st.speak())


class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @abstractmethod
    def show(self):
        pass
    
    @property
    def info(self):
        return f"Name: {self.name}, Age: {self.age}"

class Footballer(Person):
    s = [1,2,3,4,5]

    def __init__(self, name, age, team):
        super().__init__(name, age)
        self.team = team

    @property
    def show(self):
        return f"Footballer Name: {self.name}, Age: {self.age}, Team: {self.team}"

    def __str__(self):
        return f"Name = {self.name}"
    
    def __add__(self):
        return f"sum: {self.name + self.name}"
    
    @classmethod
    def change(cls, a):
        print(cls.s)
        cls.s.append(a)
        return f"{cls.s}"
    

    @staticmethod
    def helper():
        return f"this is helper"
        

f = Footballer("John", 25, "FC Barcelona")
print(f.show)
print(f.info)
print(f)
print(f.change(2))
print(f.helper())