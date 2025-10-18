from contextlib import contextmanager

class MyContext:
    def __enter__(self):
        print("Entering the context")
        return 'some value'

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")
        if exc_type:
            print(f"An exception occurred: {exc_value}")
        print("Cleanup actions can be performed here")
        return False  
    


def do_something():
    with MyContext() as context:
        print("Inside the context")
        # Uncomment the next line to simulate an exception
        # raise ValueError("An error occurred!")

do_something()



# @contextmanager
# def context_manager():
#     print('entering')
#     yield 'value'
#     print('exiting')

# with context_manager()as c:
#     print('this is context',c)