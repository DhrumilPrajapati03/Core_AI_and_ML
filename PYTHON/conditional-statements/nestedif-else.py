#syntax:
#if contidion:
    #if condition:
        #logic
    #else:
        #logic
#else:
    #if condition:
        #logic
    #else condition:
        #logic

n1 = int(input("enter the number1:")) #10
n2 = int(input("enter the number2:")) #20
n3 = int(input("enter the number3:")) #60

if n1>n2:
    if n1>n3:
        print(f"{n1} is the greatest number")
    else:
        print(f"{n3} is the greatest number")
else:
    if n2>n3:
        print(f"{n2} is the greatest number")
    else:
        print(f"{n3} is the greatest number")