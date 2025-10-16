
def my_decorator(func):
    def wrapper(*args,**kwargs):
        print('decorator started')
        result = func(*args,**kwargs)
        print('decorator ended')
        return result
    return wrapper

@my_decorator
def salom(n):
    print(n)

salom(10)