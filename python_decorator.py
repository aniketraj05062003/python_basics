
#  Decorator functions in python

def decorator(func):

    def wrapper():

        print("Welcome")

        func()

        print("Thank You")

    return wrapper

@decorator
def hello():
    print("Learning Python")
hello()


# Example 1: Welcome Message

def decorator(func):
    def wrapper():
        print("Welcome user ")
        func()
        print("Thank You")
    return wrapper

@decorator
def login():
    print("Login successful")

login()

# Example 2: Execution Time

import time

def timer(func):
    def wrapper():
        start=time.time()
        func()
        end =time.time()

        print("Time:",end-start)

    return wrapper

@timer
def program():
    for i in range(100000):
        pass
program()

# Example 3: Login Authentication

def authenticate(func):

    def wrapper():
        password = int(input("Enter password: "))
        if password==1234:
            func()
        else:
            print("Wrong password")

    return wrapper

@authenticate
def Hello():
    print("Hello admin")
Hello()


# Decorator with Arguments

def decorator(func):
    def wrapper(name):
        print("Before")
        func(name)
        print("After")

    return wrapper()

@decorator
def greet(name):
    print("Hello",name)

greet("Rahul")












    

