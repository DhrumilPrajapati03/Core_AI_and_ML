# #map example
l = [1,2,3,4,5]

# square = lambda x: x*x
# # print(square(5))

# sqlist = map(square,l)
# print(list(sqlist))

#Filter example

# def positive(n):
#     if(n%2==0):
#         return True
#     else:
#         return False

# onlypositive = filter(positive, l)
# print(list(onlypositive))

#reduce example:
from functools import reduce
def sum(a,b):
    return a+b

print(reduce(sum,l))


# l = [1,2,3,4,5]
# l = [3,3,4,5]
# l = [6,4,5]
# l = [10,5]
# l = 15

# from functools import reduce
# def sum(a,b):
#     return a+b

# print(reduce(sum,l))