#prime number- prime num divisible by 1 and itself

n=int (input("enter number"))
i=2
if(n==1):
    print(n," is not prime number")
else:
    for i in range(2,n):
        if(n%i==0):
            break
    if(n%i==0):
        print(n,"is not prime num")
    else:
        print(n,"is prime number")