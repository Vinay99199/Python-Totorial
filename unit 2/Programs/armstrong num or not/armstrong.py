#Armstrong number

n=int (input("enter number"))
s=0
rem=0
x=n
while(n>0):
    rem=n%10
    s=s+(rem*rem*rem)
    n=n//10
if(s==x):
    print(s,"is Armstrong number")
else:
    print(s,"not Armstrong number")