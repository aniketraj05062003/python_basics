
# Math Module : Math module is used for mathematical calculations
# _____________________________________________________________________

# 1. Import math module

import math

print(math.sqrt(64))

# output: 8.0

# 2. math.sqrt() — Square Root


x= math.sqrt(100)

print(x)

# output: 10.0

# 2. math.sqrt() — Square Root


x=math.pow(7,3)

print(x)

# output: 343.0

# 4. math.factorial() — Factorial


x=math.factorial(10)

print(x)

# output: 3628800

# 5. math.ceil() —Round


print(math.ceil(7.8))
print(math.ceil(2.4))

# output: 8
        # 3

# math.ceil returns next number after decimal

# 6. math.floor() —Round


print(math.floor(8.1))
print(math.floor(7.9))

# output: 8
        #   7

# math.floor returns previous number before decimal

# 7. math.fabs() — Absolute Value


print(math.fabs(-89))
print(math.fabs(-25))

# output: 89
        # 25

# 8. math.gcd() — Greatest Common Divisor : Finds HCF


HCF=math.gcd(12,18)

print(HCF)

# output: 6

# 9. math.lcm() — Least Common Multiple


LCM = math.lcm(24,26,18)

print(LCM)

# output: 936

# 10. Mathematical Constants

# import math

# print(math.pi)

# Area of Circle 


r=5

Area=math.pi*r**2

print(Area)

# output: 78.53981633974483

# 11. math.e


print(math.e)

# output: 2.718281828459045

# 12. Trigonometric Functions


print(math.sin(0))
print(math.cos(0))
print(math.tan(0))

# output: 0.0
        # 1.0
        # 0.0

# 13. Convert degree into radian


angle=math.radians(90)

print(angle)

# output: 1.5707963267948966

#  Convert radian into degree

angle =math.degrees(math.pi/2)

print(angle)

# output : 90.0

# 14. Logarithm


print(math.log(10))

print(math.log10(100))

print(math.log10(10))

# output : 
# 2.302585092994046
# 2.0
# 1.0

# 15. math.isqrt() : isqrt gives exact value without decimal


print(math.isqrt(25))  # output:5

# difference b/w sqrt and isqrt


print(math.sqrt(25))  # output: 5.0
print(math.isqrt(25)) # output: 5

# 16. math.comb() — Combinations


combinations = math.comb(5,4)

print(combinations)

# output : 5

# Formula : 5C4 =5

# 17. Example — Circle Area


radius = float(input("Enter radius: "))

area = math.pi*radius**2

print("Area: ",area)

# if enter radius: 6

# output: 113.09733552923255

