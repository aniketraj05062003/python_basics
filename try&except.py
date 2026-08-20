
#  try and except

try:
    x="10+a"
    print(x)

except:
    print("this variable is not defined")

# Avoid Error while dividing zero to a number

try:
   result = 10/0
   print(result)

except:
    print("You Can not divide a number by zero ")

# valid division

try:
    result = 20/5
    print(result)

except:
    print("Invalid division")


# user input

try:
    num = int(input("Enter Number"))
    print(num)

except:
    print("Enter numbers only")

# specific exception

try:
    result = 10/0
    print(result)

except ZeroDivisionError:
    print("Division by zero is not allowed")

# Multiple Exceptions

try:
    num=int(input("Enter num :"))
    result = 100/num
    print(result)

except ValueError:
    print("Enter a valid number")

except ZeroDivisionError:
    print("Division by zero is not allowed") 

# else Block


try:
    number= int(input("Enter num: "))
except ValueError:
    print("Invalid input")
else:
    print("You enterd", number)

# finally block

try:
    result=10/2
    print(result)

except:
    print("Error")
finally:
    print("Program finished")
