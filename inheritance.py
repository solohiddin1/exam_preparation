class Student:
    school_name = "HighTech School"   # class attribute (shared by everyone)

    def __init__(self, name, grade):
        self.name = name              # instance attribute
        self.grade = grade            # instance attribute

    # 1️⃣ Instance Method — works with each student's data
    def get_info(self):
        return f"{self.name} studies in grade {self.grade} at {self.school_name}"

    # 2️⃣ Class Method — works with the whole class (shared data)
    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name

    # 3️⃣ Static Method — helper logic, not tied to any data
    @staticmethod
    def is_passing(mark):
        return mark >= 60


# Create students
s1 = Student("Alice", 10)
s2 = Student("Bob", 9)

# Instance method (uses self)
print(s1.get_info())  # Alice studies in grade 10 at HighTech School

# Class method (uses cls)
Student.change_school("Future Academy")
print(s2.get_info())  # Bob studies in grade 9 at Future Academy

# Static method (no self or cls)
print(Student.is_passing(75))  # True
print(Student.is_passing(40))  # False



# class Person:
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age
    
#     def info(self):
#         return f"{self.name}"
    

# class Student(Person):
#     def __init__(self, name, age, grade):
#         super().__init__(name, age)
#         self.grade = grade
    
# st = Student("name1",4,5)
# print(st.info())