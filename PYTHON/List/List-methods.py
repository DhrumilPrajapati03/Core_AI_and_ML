l = [10,20,30,"p",98.7,"apple",True,67.5]
j = [50,60,70,80,50,60,60,60,20]

print(j.count(60))

#for adding any object at the end of the list
l.append(40)
print(l)

#at particular index number
l.insert(0,90)
print(l)

#remove objects from the list
l.pop()
print(l)

#particular object
l.remove("p")
l.remove("apple")
l.remove(True)
print(l)

#empty
# l.clear()
# print(l)

#reverse
l.reverse()
print(l)

#sort method
l.sort()
print(l)
l.sort(reverse=True)
print(l)

#extend method
j.extend(l)
print(l)