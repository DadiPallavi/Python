#Write a program that takes array of numbers as input, among the numbers in array, print the numbers which forms a prime number by adding one to it. Print such numbers in the given array separated b spaces.

             # Testcase1	:  [ 7, 4, 7, 23, 10, 6]
              # Output     	:  4 10 6
a=[7,4,7,23,10,6]
count=0
for i in a:
    j=i+1
    for k in range(1,j+1):
        if j%k == 0:
            count+=1
    if count<=2:
        print(i)




