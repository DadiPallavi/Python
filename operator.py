#Create a simple calculator that takes in two numbers and an operator (+, -, *, /) 
# and performs the operation based on the operator, handling division by zero errors using conditional statements.
n1=int(input("Enter the number: "))
n2=int(input("Enter the number: "))
op=input("Enter operator (+, -, *, /): ")
if op=="+":
    print("additon: ",n1+n2)
elif op=="-":
    print("sub: ",n1-n2)
elif op=="*":
    print("product: ",n1*n2)
elif op=="/":
    print("Divsion: ",n1/n2)
else:
    print("u gave unidentified operator")
    