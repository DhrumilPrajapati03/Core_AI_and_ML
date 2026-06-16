t = ('10',20, True, "Hello", 3.14) #immutable
print(type(t))

for i in t:
    if i== True:
        print(i)

print(t.index(3.14))
print(t.count(10))

k = list(t)
k.append(40)
t = tuple(k)
print(t)

# t[2]  = False
# print(t)
   
l = [10,20, True, "Hello", 3.14] #mutable
l[2] = False
print(l)

# L = (i for i in range(-20,20) if i%2==0)
# print(tuple(L))

