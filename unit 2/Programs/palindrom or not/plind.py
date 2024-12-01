
n=int(input("Enter a number"))
y=n
rev=0
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
print(rev)
if(rev==y):
    print(" is palindrom")
else:
    print("is not palindrom")