# num = int(input("enter the number:"))

# if num>0:
#     print("positive")
# elif num<0:
#     print("negative")
# else:
#     print("zero")

#<34 -> fail
#>34-<65 -> distinction
#>65-<75 -> second class
#>75-<90 -> first class
#>90-<100 -> excellent


marks = int(input("enter the marks:"))

if marks<34:
    print("fail")
elif marks>34 and marks<65:
    print("distinction")
else:
    print("invalid")