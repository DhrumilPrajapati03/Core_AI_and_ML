# def fact(n): #3
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1) #5*4*3*2*1
    
# factorial = fact(5)
# print(f"factorial of given number is {factorial}")

def sum_list(numbers):
  if len(numbers) == 0:
    return 0
  else:
    return numbers[0] + sum_list(numbers[1:]) #1 + 2 + 3+ 4+ 5 + 0

my_list = [1, 2, 3, 4, 5]
print(sum_list(my_list))