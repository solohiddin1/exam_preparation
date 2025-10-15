class Number:

    def __init__(self,number):
        self.number = number

    def __add__(self,other):
        return self.number + other.number
    
    # def __str__(self):
    #     return f"number is {self.number} "
    
    def __repr__(self):
        return f"Number is ->({self.number})"

a = Number(10)
b = Number(8)
print(a)
print(b)
print(a + b)