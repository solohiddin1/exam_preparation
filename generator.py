
def generator(n):
    count = 0
    while count < n:
        yield count
        count += 1
    # return count
    # yield count


# i = generator(20)
# print(next(i))

l = [1,2]
it = iter(l)
try:
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
except StopIteration:
    print('no left')



# l.__iter__()

# comparison 
# import sys 
# squares = [i ** 3 for i in range(10_000_000)]
# squares_gen = (i ** 3 for i in range(10_000_000))
# print('list',sys.getsizeof(squares))
# print('generator',sys.getsizeof(squares_gen))
# print('recursion limit', sys.getrecursionlimit())
# print(type(squares))
# print(type(squares_gen))