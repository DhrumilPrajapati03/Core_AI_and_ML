s = "{noun} love eating {type} cheese and {item} sandwiches."

#positional formatting
# x1 = s.format("We")
# print(x1)

#multiple parameters
# x2 = s.format("we", "roasted", "paneer")
# print(x2)

#order of parameters
            #  0       1          2
# x3 = s.format("we", "roasted", "paneer")
# print(x3)

#alias within the string
# x4 = s.format(noun="I", type="roatesd", item="garlic")
# print(x4)

#f-string
a = int(input("enter the value:"))
b = int(input("enter the value:"))

addition = a+b
print(f"addition of {a} and {b} is {addition}")