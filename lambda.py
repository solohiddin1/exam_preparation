
s = [1,2,3,4,5]

# res = list(map(lambda x: x**2, s))

# res = list(map(s))

# print(res)


# inp = list(map(int, input("Enter numbers separated by space: ").split()))
# ins = 5
# imp1 = list(filter(lambda x: x % 2 == 0, inp))
# a, b, c, d, e = map(int, input("Enter numbers separated by space: ").split())

# print(a, b, c, d, e)

# print(inp)
# print(res)

res = [i for i in range(5)]
print(res)


l = [1,2,3,4]
res = list(map(lambda x:x**2 , l))
print(res)

filter1 = list(filter(lambda x: x % 2 == 0, l))
print(filter1)