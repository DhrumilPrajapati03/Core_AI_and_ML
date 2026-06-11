#Area of triangle
def aot(b,h):
    return 0.5 *b * h

print(aot(5,6))

#Prime number
def is_prime(n):
    if n == 0 or n == 1:
        print(f"{n} is not prime")
    elif n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                print(f"{n} is not prime")
                break
        else:
            print(f"{n} is a prime number")
    else:
        print(f"{n} is not prime")

is_prime(17)

#reverse a string
def reverse_string(s):
    return s[::-1]

entered_string = input("Enter a string: ")
print(reverse_string(entered_string))

#Greatest of Four
def greatestO4(n1,n2,n3,n4):
    if n1>n2:
        f1 = n1
    else:
        f1 = n2 #453 

    if n3>n4:
        f2 = n3
    else:
        f2 = n4 #76

    if f1>f2:
        print(f"{f1} is greatest")
    else:
        print(f"{f2} is greatest")

greatestO4(23,453,54,76)

# area of circle
def aoc(r):
    return 3.14*r*r

print(aoc(2))