# Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February.
# This is how to work out whether if a particular year is a leap year:
# on every year that is evenly divisible by 4 
# **except** every year that is evenly divisible by 100 
# **unless** the year is also evenly divisible by 400

# e.g. The year 2000: 2000 ÷ 4 = 500 (Leap), 2000 ÷ 100 = 20 (Not Leap), 2000 ÷ 400 = 5 (Leap!)
# So the year 2000 is a leap year.
# But the year 2100 is not a leap year because: 2100 ÷ 4 = 525 (Leap), 2100 ÷ 100 = 21 (Not Leap), 2100 ÷ 400 = 5.25 (Not Leap)
# e.g. 2000, 2004, 2008, 2012, 2016 are leap years

year = int(input("Which year do you want to check? "))

# The modulo is written as a percentage sign (%) in Python gives the remainder after a division.
if year % 4 == 0:
  if year % 100  == 0:
    if year % 400 == 0:
      print("This is a leap year.")
    else:
      print("This is a normal year.")
  else:
    print("This is a leap year.")
else:
  print("This is a normal year.")