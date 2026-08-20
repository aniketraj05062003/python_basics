

# while loop revision in python
# ________________________________

# Printing "Hello world" 50 times using while loop

i=1

while i <=50:
    print("Hello world")
    i+=1

# Printing list value its len times

list = ["ram","shyam","mohan","sohan"]

i=0

while i < len(list):
    print(list[i])

    i+=1

# * finding sum of all numbers in a list

num = [10,20,50,60,58]

i=0
total=0

while i < len(num):
    total=total+num[i]
    i+=1
print("Total: ",total)

# break statement

i=0

while i <6:
    print(i)
    if i ==3:
        break
    i+=1

# continue statement

i=0

while i <6:
    i+=1
    if i==3:
        continue
    print(i)

# it will skip 3 and continue after 3


# checking even number betwen 1 to 10

num =1 

while num <=10:
    if num%2==0 :
        print(num)
    num +=1


# checking odd number between 1 to 10

num =1 

while num <=10:
    if num%2!=0:
        print(num)
    num+=1


# Prime number program

# num = int(input("Enter num: "))

i = 2
count =0

while i < num:
    if num % i ==0:
        count = count+1

    i=i+1

if count == 0:
     print("Prime number")

else:
    print("Not a prime Number")

# odd number program

num =int(input("Enter num: "))

if num % 2 !=0 :
    print(num,"is an odd number")
else:
    print(num, "is not an odd number")

# Even number program

num = int(input("Enter Your num: "))

if num % 2 == 0:
    print(num, "is an even number")
else:
    print(num,"is not an even number")

# prime number program

num = int(input("Enter num: "))

i =2
count =0

while i < num:
    if num % i == 0:
        count=count+1

    i=i+1

if count == 0:
    print(num,"is a Prime Number")
else:
    print(num,"is not a prime Number")

# check large numbers 

num =[99,55,98,85,52,45]

i =0

largest = num[0]

while i < len(num):
    if num[i] > largest:
        largest=num[i]
    i=i+1

print("Largest Number: ",largest)


# check positive and negative number

numbers = [10, -5, 20, -8, 15, -2]

i =0

while i < len(numbers):
    if numbers[i]>=0:
        print(numbers[i],"is a positive number")
    else:
        print(numbers[i],"is a  negative number")
    i=i+1


# check smallest number 

num =[99,55,98,85,52,45]

i = 0
smallest = num[0]

while i < len(num):
    if num[i] < smallest[0]:
        smallest=num[i]

    i=i+1

print("Smallest Number : ",smallest)


# Print numbers from 1 to 10.

i = 1 

while i <=10:
    print(i)

    i = i+1

# Print numbers from 5 to 1

i=5

while i >=1:
    print(i)
    i = i-1

i = 16

while i >= 2:
    print(i)
    i = i // 2












     

 






