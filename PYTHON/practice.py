l=[1,2,3,4,5,6]
l2=[7,8,9,10,11]
# l3=l1 + l2
# print(l3)

# l=int(input("enter the number"))
def max_min(l):
    if len(l) == 0:
        print(0)
    else:
        l.sort(reverse=True)
        print("max number:",l[0])

    if len(l) == 0:
        print(0)
    else:
        l.sort()
        print("min number:", l[0])

max_min(l)

min(l)
max(l)

