
# Revision of recrusion
# -------------------------


def countdown(n):
    if n<=0:
        print("done!")
    else:
        print(n)
        countdown(n-1)
countdown(5)

# Identifying base case and recursive case:

def factorial(n):
    if n==0 or n==1:           #Base case
        return 1
    else:
        return n*factorial(n-1)  # recursive case

print(factorial(5))


# Find the 7th number in the Fibonacci sequence:

def febonacci(n):
    if n<=1:
        return n 
    else: 
        return febonacci(n-1)+febonacci(n-2)

num = int(input("Enter number: "))
print(febonacci(num))

# Recursion with list

# calculate all the values in the list_

def sum(numbers):
     if len(numbers)==0:
          return 0 
     else:
          return numbers[0]+sum(numbers[1:])

list =[45,48,50,55]
print(sum(list))


# Find the maximum value in the list_


def max_value(numbers):
    if len(numbers)==1:
        return numbers[0]
    else:
        max_of_rest=max_value(numbers[1:])
        return numbers[0] if numbers[0]>max_of_rest else max_of_rest

mylist =[5,85,45,75]
print(max_value(mylist))