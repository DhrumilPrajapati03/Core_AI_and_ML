    #0      1       2      3
l = [10, "apple", 92.5, True]
# print(l)
# print(type(l))
print(l[1])
print(l[2])
print(l[3])
print(l[0])

x = l[:]
print(x)
#mutable and immutable 
s = "water is very clean" #immutable
# s[1] = "o"
# print(s)

l = [10, "apple", 92.5, True] #mutable
l[1] = 87.9
print(l)