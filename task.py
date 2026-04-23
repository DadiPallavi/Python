#  Global Variables
g1 = "Global 1"
g2 = "Global 2"
g3 = "Global 3"
#  Function 1
def func1():
    a = "Local A (func1)"
    
    print("Inside func1:")
    print(a)     
    print(g1)    
    print(g2)
    print(g3)

#  Function 2
def func2():
    b = "Local B (func2)"
    
    print("\nInside func2:")
    print(b)     
    print(g1)    
    print(g2)
    print(g3)
    



#  Function 3
def func3():
    c = "Local C (func3)"
    
    print("\nInside func3:")
    print(c)     
    print(g1)    
    print(g2)
    print(g3)
    



#  Function Calls
func1()
func2()
func3()



print("\nOutside functions:")



print(g1)
print(g2)
print(g3)