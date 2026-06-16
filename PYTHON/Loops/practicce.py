n = int(input("ente the number: "))

# for i in range(10,0,-1):
#     print(n, "x" , i, "=", n*i)

# l = ["harry", "Soham", "Sachin", "Rahul"]

# for i in l:
#     if i.startswith("S"):
#         print("hello", i)
# x=1
# while x<11:
#     print(n, "x" , x, "=", n*x)
#     x+=1 # x = x+1

# if n == 0 or n == 1:
#     print(f"{n} is not prime")

# elif n>1:
#     for i in range(2,n):
#         if (n%i)==0: 
#             print("not prime")
#             break
#     else:
#         print(f"{n} is prime number")

# else:
#     print("not prime")


# +2+3+4+5+6+7+8+9+10 = 55

# total = 0
# while n>0: #0
#     total += n #total = total+n = 14+1 = 15
#     n -= 1 # n = 1-1 = 0
# print(total)

factorial = 1
for i in range(1,n+1):
    factorial*=i
print(factorial)