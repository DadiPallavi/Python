#Implement a program that asks the user for their age and then tells them if 
# they are eligible to vote based on a minimum voting age of 18.
age=int(input("Enter your age:"))
if age>=18:
    print("your are egible to vote")
else:
    print("your are not egible to vote")