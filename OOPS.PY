
#  OOP :object oriented programming
# ____________________________________________________

# Create a Class

class Myclass:
    x=5
print(Myclass)

# Create Object

p1=Myclass()

print(p1.x)

# Delete Objects

# del p1

# Multiple Objects

class Myclass:
    x=5
p1=Myclass()
p2=Myclass()
p3=Myclass()

print(p1.x)
print(p2.x)
print(p3.x)

# Python __init__() Method (Constructor)

class person:
    def __init__(self,name,city,age):
        self.name=name
        self.city=city
        self.age=age

p1=person("Aniket","New Delhi",23)

print(p1.name)
print(p1.city)
print(p1.age)

# Create a class without __init__():

class person:
    pass

p1=person()
p1.name="Aniket"
p1.age=23

print(p1.name)
print(p1.age)

# With __init__(), you can set initial values when creating the object:

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=person("Aniket",23)

print(p1.name)
print(p1.age)

# Default Values in __init__()

class Person:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age

p1 = Person("Emil")
p2 = Person("Tobias", 25)

print(p1.name, p1.age)
print(p2.name, p2.age)

# Multiple Parameters

class person:
    def __init__(self,name,age,city,country):
        self.name=name
        self.age=age
        self.city=city
        self.country=country

p1=person("Aniket",23,"New Delhi","India")

print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)

# The self Parameter

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def greet(self):
        print("Hello my name is "+ self.name)

p1=person("Aniket",23)
p1.greet()

# Access multiple properties using self:

class car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    def display_info(self):

     print(f"{self.year} {self.brand} {self.model}")

car1=car("Toyota","corolla",2020)

car1.display_info()

# Calling Methods with self: Call one method from another method using self:

class person:
    def __init__(self,name):
        self.name=name

    def greet(self):
        return "Hello ,"+self.name

    def welcome(self):
        message=self.greet()
        print(message+"! Welcome to our website.")

p1=person("Aniket")
p1.welcome()


# # Class Polymorphism


class car:
    def __init__(self,brand, model):
        self.brand=brand
        self.model=model

    def move(self):
        print("!drive")

class boat:
    def __init__(self,brand, model):
        self.brand=brand
        self.model=model

    def move(self):
        print("!sail")

class plane:
    def __init__(self,brand, model):
        self.brand=brand
        self.model=model

    def move(self):
        print("!fly")


# # create an object

car1 = car("Ford", "Mustang")        
boat1 = boat("Ibiza", "Touring 20")  
plane1 = plane("Boeing", "747")

for x in (car1,boat1,plane1):
    print(x.brand)
    print(x.model)
    x.move()


# # Python Encapsulation get properties

class person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age

    def get__age(self):
        return self.__age

p1=person("ram",25)

print(p1.name)
print(p1.get__age())


# # Set Private Property Value

class person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if age>0:
            self.__age=age
        else:
            print("age all must positive")


p1=person("ram",25)

print(p1.name)
print(p1.get_age())

p1.set_age(-10)
print(p1.name)
print(p1.get_age())

# Inheritance + polymorphism 

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")        
boat1 = Boat("Ibiza", "Touring 20")  
plane1 = Plane("Boeing", "747")      

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()











