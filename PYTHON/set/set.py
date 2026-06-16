d = set()
s = {1,2,3,3,3,3,4,54,6,7,2,1,1,12}
print(s) 
t = set([1,2,3,4,5,6,7,8,9])
print(t)
t[2] = 100
print(t)

f = s.intersection(t)
print(f)

j = s.union(t)
print(j)

l = s.difference(t)
print(l)

o = t.difference(s)
print(o)
# s.add(100)
# print(s)    

# s.remove(100)
# print(s)

# s.pop()
# s.pop()
# s.pop()
# print(s)
# # s.clear()
# # print(s)

# k = s.copy()
# print(k)

L = {i for i in range(-20,20) if i%2==0}
print("L:", L)