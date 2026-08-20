# for loop in python

fruits = ["apple", "banana", "cherry"]

for i in fruits:
    print(i)


# # tuple=("ram","shyam","mohan")

# string

name="python"

for x in name:
    print(x)

# break statement

fruits = ["apple", "banana", "cherry"]

for i in fruits:
    
    if i=="banana":
        break
    print(i)


# # continue statement

fruits = ["apple", "banana", "cherry"]
for i in fruits:
    
    if i=="banana":
        continue
    print(i)


# range() function

name="aniket"

for i in range(2,30,3):
    print(i)


# # nested for loop

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x,y)

# star  pattern

for i in range(1,6):
    for j in range(i):
        print("*", end="")
    print()

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# for x in [0, 1, 2]:
#     pass

# table program

num=int(input("Enter num: "))

for i in range(1,11):
    print(num,"x",i, "=",num*i)   


# Even number print ( 1-20 )

for x in range(2,21):
    if x%2==0:
        print(x)

# odd number print (1-20)

for x in range(1,21):
    if x%2!=0:
        print(x)

# Table Program

num=int(input("Enter num: "))

for i in range(1,11):
    print(num,"x",i,"=",num*i)

# sum program

total=0
for i in range(1,11):
    total=total+i
    print("Total:",total)

# factorial program

num = int(input("Enter num: "))

factorial =1

for i in range(1,num+1):
    factorial=factorial*i
print("factorail: ",factorial)

# prime number check

num = int(input("Ener your number: "))

count = 0

for i in range(1,num+1):
    if num%i ==0:
        count = count+1

if count == 2:
    print(num ,"is a Prime number")
else:
    print(num, "is not a prime number")

# nested for loop: star pattern

for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()

# •	Outer loop → Rows 
# •	Inner loop → Stars 


# nested for loop: star pattern

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


# find large number in this list


num =[50,52,65,98,99,105,85,850,725]

largest =num[0]

for i in num:
    if i > largest:
        largest=num
print("largest num is: ",largest)

# count vowel in this string

text = "programming language"

count = 0 

for char in text:
    if char in "aeiou":
        count= count+1
print("Total vowels: ",count)




