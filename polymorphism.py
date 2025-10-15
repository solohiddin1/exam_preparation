class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return f"{self.name} is {self.age} years old."

class Student(Person):
    def info(self):
        return f"Student: {self.name}, Age: {self.age}, I'm a student."

class Teacher(Person):
    def info(self):
        return f"Teacher: {self.name}, Age: {self.age}, I'm a teacher."

people = [
    Teacher("Bob", 40),
    Student("Charlie", 22),
    Teacher("Diana", 35)]

for p in people:
    print(p.info())
    