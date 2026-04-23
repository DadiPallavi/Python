#Write a python program to remove the duplicate in given list.
              #  a = [2,3,4,2,3,4,5,7]
               # output: [2,3,4,5,7]

a=[2,3,4,2,3,4,5,7]
b=[]
for i in a:
    if i not in b:
        b.append(i)

print(b)
