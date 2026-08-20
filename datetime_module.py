
#  Pyhton module : datetime
# _____________________________________

# 1. import datetime module

import datetime


# 2. Current date + Time


print(datetime.datetime.now())

# 3. Current Date


today = datetime.date.today()

print(today)

# Output: Today's date ex- 2026-08-13

# 4. Current Time


current_time= datetime.datetime.now().time()

print(current_time)

# Displays current_time in output

# 5. Current Date + Time


now = datetime.datetime.now()

print(now)

# Displays both current date and time

# 6. date Object : Creating date manually


dob = datetime.date(2026,5,15)

print(dob)

# Output : 2026-05-15

# 7. Extractung Parts of date  : Extracting year, month,day from date


date = datetime.date(2026,5,25)

print(date.year)
print(date.month)
print(date.day)


# 8. datetime Object: can create date and time manually


date = datetime.datetime(2026,5,26,21,43,26)

print(date)

# 9. strftime() — Date ko Format Karna


now =datetime.datetime.now()

print(now.strftime("%d-%m-%Y"))


# 10. strptime() — String ko Date mein Convert Karna

datestr="04/04/1996"

date1=datetime.date.strptime(datestr,"%d-%m-%")
print(date1)


# 11. Date Difference


date1= datetime.date(2026,8,11)
date2= datetime.date(2027,7,1)

differnce = date2-date1

print(differnce)

# OUtput : 324 days

# 12. timedelta : timedelta ka use date/time mein days, weeks, hours etc. add/subtract karne ke liye hota hai.

# Adding 10 days 


today = datetime.date.today()

future_date=today+datetime.timedelta(days=10)

print(future_date)

# 13. Subtract 10 Days 


today = datetime.date.today()

Future_date = today-datetime.timedelta(days=10)

print(Future_date)

# 14. Add 2 Weeks 


today = datetime.date.today()

future_date = today + datetime.timedelta(weeks=2)

print(future_date)

# 15. Add 5 Hours  


now = datetime.datetime.now()

future_time = now+datetime.timedelta(hours=5)

print(future_time)

# 16. Add 30 Minutes 

# import datetime

now = datetime.datetime.now()

future_time= now+datetime.timedelta(minutes=30)

print(future_time)

# calculating total age using DOB


dob =datetime.date(2003,6,5)

today=datetime.date.today()

age = today.year-dob.year

if (today.month,today.day)<(dob.month,dob.day):

    age -=1

print("Age : ",age)






