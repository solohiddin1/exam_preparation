
# Bank class
class Bank:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{self.owner}, Deposited: {amount}")
        else:
            print(f"{self.owner}, Deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{self.owner}, Withdrew: {amount}")
        else:
            print(f"{self.owner}, Insufficient funds or invalid amount")

    def get_balance(self):
        return self.__balance
    
# Example usage:
# bank = Bank("Alice", 100)
# print(bank.get_balance())  # This will work
# bank.deposit(50)
# bank.withdraw(30)
# print(bank.get_balance())  # This will work
# print('-' * 20)

# Student class
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.__grade = grade

    def get_name(self):
        return self.name
    
    def get_grade(self):
        return self.__grade
    
    def set_grade(self,new_grade):
        if new_grade in ['A','B','C']:
            self.__grade = new_grade
            return f"{self.__grade} grade set"
        else:
            return 'Invalid'

# Example usage:
# student = Student("Bob", "A")
# print(student.get_grade()) 
# print(student.set_grade('B')) 
# print(student.get_name()) 
# print(student.get_grade()) 
# print('*'*40)
# print(student.__grade)  


# Access Modifiers
class Example:
    def __init__(self):
        self.public = "I'm public"
        self._protected = "I'm protected (by convention)"
        self.__private = "I'm private (name mangled)"
e = Example()
# print(e.public)
# print(e._protected)
# print(e._Example__private)

# print('-'*30)



# property decorator
class Car:
    def __init__(self):
        self.__engine_started = False

    @property
    def start(self):
        self.__check_fuel()
        print(self.__check_fuel())
        self.__engine_started = True
        print('engine started!')
    
    def __check_fuel(self):
        return 'checking fuel--'
# print('car')
# c = Car()
# c.start




class Animal:
    species = "Canis familiaris"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute
    
    def bark(self):
        return f"{self.name} says Woof! I am {self.age} years old."
    
    @classmethod
    def class_info(cls,new_species):
        cls.species = new_species
        return f"All dogs are of species: {cls.species}"
a = Animal("Buddy", 3)
b = Animal("puppy", 1)

print(a.bark())
print(b.bark())

print(Animal.class_info("Canis lupus familiaris"))
print(a.class_info("Canis lupus"))












# Function Decorators
# import time

# def decorator(func):
#     def wrapper(*args , **kwargs):
#         start = time.time()
#         print("before")
#         res = func(*args, **kwargs)
#         print(say_hello.__name__)
#         print("after")
#         end = time.time()
#         print("time:", end - start)
#         return res
#     return wrapper

# @decorator
# def say_hello(a,b):
#     return a+b

# # say_hello = decorator(say_hello)
# print(say_hello(1, 2))
