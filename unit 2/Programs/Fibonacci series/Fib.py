n=int(input("Enter term "))
n1,n2=0,1
if(n<=0):
    print("please a positive number")
elif(n<=1):
    print("fibnaocci series is ")
    print(n1)
elif(n<=2):
    print("fibnaocci series is ")
    print(n1)
    print(n2)
else:
    print(n1)
    print(n2)
    for i in range (2,n):
        n3=n1+n2
        print(n3)
        n1=n2
        n2=n3
