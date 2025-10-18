
def my_decorator(func):
    def wrapper(*args,**kwargs):
        print('decorator started')
        func(*args,**kwargs)
        add = sum(args)
        add1 = sum(kwargs.values())
        print('1= ',add)
        print('2= ',add1)
        print('decorator ended')
        return func
    return wrapper

@my_decorator
def salom(n,d,l = 1):
    print(n)

salom(10,12,l=2)