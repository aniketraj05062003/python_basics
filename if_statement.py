
# If statement
# ----------------------------

a=int(input("Enter First Num:"))
b=int(input("Enter Second Number:"))

if a > b :
    print("a is greater than b")

# if elif statement
# ----------------------------


a=int(input("Enter First Num:"))
b=int(input("Enter Second Number:"))

if a > b :
    print("a is greater than b")

elif a==b :
    print("a is equal to b b")

elif a < b :
    print("a is less than b")

# if and else statement 
# ----------------------------


age=int(input("enter your age:"))

if age >=18 :
    print("You are eligible to vote")

else :
    print("You are not eligible to vote")


# Nested if Statement
# ----------------------------

attendance=int(input("enter your attendance:"))
experience=int(input("enter your exp:"))

if attendance >=85:
    if experience >=3 :
       print("You are eligible to get Promotion")
else:
    print("You are not eligible to get promotion")

a=40
b=30

if a > b: print("a is greater than b")

x=10
y=5

max_value= x if x>y else y
print("maximum value", max_value)


# # logical operator with if statement
# ----------------------------


age=int(input("enter your age: "))

has_vote_id= True

if age >=18 and not has_vote_id:

    print("you can vote")

else:
    print("you can't vote")


# "if and elif " with logical operator
# ___________________________________________________

# 1. person whose age is >=18 and has voter id then he can vote

age = int(input("enter your age "))
has_voter_id = True

if age >=18 and has_voter_id:
    print("You can vote")

else:
    print("You can't vote")

# 2. A student is eligible for examintation if he has 33 or more than 33 marks and 75 or more than 75 attendance

marks = int(input("Enter your marks: "))
attendance = int(input("Enter your attendance: "))

if marks >=33 and attendance >=75 :
    print("You are eligible for exam")

else: 
    print("You aren't eligibel for exam")


# 3. You will able to login only if you have correct username and password

username ="aniket05"
password = "aniket@123"

if username == "aniket05" and password == "aniket@123":
    print("Logged in successfully")

else:
    print("invalid username or Password")


# 4. if day is sat or sun then it's holiday otherwise it's working day

day = "sunday"

if day == "sunday" or day == "saturday":
    print("Today is holiday")
else:
    print("Today is working day")

# 5. if student has 33 or more than 33 marks or got grace marks then student is pass otherwise fail

marks = int(input("Enter your marks "))
grace_marks = True

if marks >= 33 or grace_marks:
    print("student is pass")
else:
    print("student is fail")

# 6. Rain check with not operator

is_raining = False

if  not is_raining:
    print("you can go outside")
else:
    print("Take an umbrella")














  