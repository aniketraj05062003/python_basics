

#  Regular expression 
# ____________________________________

# 1. Import the re Module

import re

text = "python is easy to learn"

result = re.search("python",text)

print(result)

# 2. If the pattern is not found:


text = "pyhton is easy to learn"

result=re.search("java",text)

print(result)

# output is none because java is not present within the text

# 3. Important RegEx Functions

# re.search()
# re.match()
# re.findall()
# re.finditer()
# re.split()
# re.sub()
# re.fullmatch()

# 4. re.search(): searches for a pattern anywhere in a string


text = "I am learning python"

result=re.search("python",text)

if result:
    print("Found")
else:
    print("Not found")

# 5. re.match(): rematch() checks string only from the beginning


text = "I love python"

result= re.match("python",text)

print(result)

# output is none because python is not at the beginning

# difference:

# search() → searches anywhere
# match()  → searches only from beginning

# 6. re.findall(): findall returns all matching value as a list


text = "python is easy. python is powerful"

result = re.findall("python",text)

print(result)

# 7. Finding Numbers: this is the most common regEX character for digits (/d)

# /d means any digit from 0 to 9


text = "My age is 25"

result=re.findall(r"\d",text)

print(result)

# to find the complete number

result = re.findall(r"\d+",text)

print(result)

# 10. Character Classes

# case-1.  \d= digit


text=re.findall(r"\d+","Price:500")

print(text)

# case=2- \D = string

text=re.findall(r"\D+","ABC123")

print(text)

# case 3. \w=word character

text = re.findall(r"\w+","Hello Python")

print(text)

# 11. Character Set []


text = "cat bat rat"

result = re.findall(r"[cbr]at",text)

print(result)

# 12. Range


text = "Python123"

result = re.findall(r"[A-Z]",text)

print(result)

# 13. + Quantifier


text = "abc12345"

result= re.findall(r"\d+",text)

print(result)

# 14. * Quantifier


text = "abc12345"

result= re.findall(r"\d*",text)

print(result)

# 15. ? Quantifier


text = "color colour"

result = re.findall(r"colo?r",text)

print(result)

# 16. {n} : Matches exactly n occurrences.


phone = "7782031665"

result = re.fullmatch(r"\d{10}",phone)

if result:
    print("Valid Phone number")

else:
    print("Invalid Phone number")

# 17. {n,m}
 

text = "12 123 12345 123456"

result= re.findall(r"\d{2,5}",text)

print(result)

# 18. ^ Beginning : checks the beginning of the text(string)
 

text = "Python is powerful"

Result = re.findall(r"^Python",text)

print(Result)

# it matches because python is at the beginning

# 19. $ End : checks the end of the string


text ="I love python"

result = re.search(r"python$",text)

print(result)


# 20. . Dot : Matches almost any single character


text = "cat cut cot"

Result = re.findall(r"c.t",text)

print(Result)

# 21. OR Operator |

text = "I like Python and Java"

result = re.findall(r"Python|Java", text)

print(result)

# 22. Groups () : Parentheses are used to create groups



text = "Name:Rahul, Age:25"

result= re.findall(r"Name:(\W+), Age:(\d+)",text)

print(result.group(1))

# 23. re.sub() — Replace Text



text = "I love Java"

result = re.sub(r"Java", "Python", text)

print(result)

# 24. re.split()



text = "apple,banana;orange mango"

result = re.split(r"[,; ]", text)

print(result)

# 25. Email Validation



email = "student@gmail.com"

pattern = r"^[\w.-]+@[\w.-]+\.\w+$"

if re.fullmatch(pattern,email):
    print("valid email")

else: 
    print("Invalid email")

# 26. Extract Phone Numbers



text = "contact us at 7782031665 or 8083130829"

result = re.findall(r"\d{10}",text)

print(result)

# 27. Extract Dates



text = "Today is 19-08-2026"

date = re.findall(r"\d{2}-\d{2}-\d{4}",text)

print(date)

# 28. Extract Prices



text = "Pen ₹50, Book ₹250, Bag ₹1200"

prices = re.findall(r"₹\d+", text)

print(prices)



