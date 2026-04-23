def prime():
    r=int(input("enter the number:"))
    count=0
    print()
    for i in range(1,r+1):
       if i>1:
        for num in range(2, i):
            if i % num == 0:
               break
        else:
            print(i)
prime()
