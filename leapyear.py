#Develop a program that determines whether a given year is a leap year or not, 
# using conditional statements to apply the rules for leap years.

year=int(input("Enter the year:"))

if(year % 4==0 and year % 100 !=0) or (year % 400 == 0):
    print(year," is a leap year")
else:
    (year," is not a leap year")