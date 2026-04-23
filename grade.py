#Write a function that takes a grade (from 1 to 100) as input and returns a string 
# indicating whether the grade corresponds to a fail (below 50), pass (50-69),
#  good (70-84), or excellent (85 and above).
 
marks=int(input("enter your marks: "))
if marks < 50:
    print("You are falied")
elif marks>=50 and marks<=69:
    print("You are pass")
elif marks>=70 and marks<=84:
    print("You got good marks")
else:
    print("You got excellent marks")