
#operators---------------------------------------------------
#1-Arithmetic operators
a=1+2
b=2-1
c=3*2
d=4/2
e=4//2
f=10%2
g=2**3
print(a ," ",b," ",c," ",d," ",e," ",f," ",g)
print()

#2-Assignment operators
a=2
b+=3
c-=4
d*=4
e/=5
f//=10
g%=5
h=a**3      # h**=2 is wrong
print(a,' ',b," ",c," ",d," ",e," ",f," ",g," ",h)
print()

#3-Bitwise  operators
a=1^2  #1=01 &  2= 10 different bit will be 1 in adding
b=2&1
c=3|2
d=~6 # ~6=-7   ,  ~3=-4  ,~8=-9
e=4<<2  #4= 100 after 10000 = 16
f=8>>2 #8= 1000 after 1000 = 16 
g=2**3
print(a ," ",b," ",c," ",d," ",e," ",f," ",g)
print()

#4-Logical operators
a=4>7
b=2<1
c=4>2
print("a and b is",a and b) #False
print("a and b is",a or c)  #True
print("a and b is",not(a and b))  #True

#5-comparison operators
n=4
m=8
a=(n==m) #False
b=n<m  #True
c=n>m #False
d=(6!=4)  #True
e=(n<=m)  #True
f=(m>=n) #True
print(a ," ",b," ",c," ",d," ",e," ",f)
print()

#6-Membership operators
a=(2,3,4,5,6,)
b="ram"
print(2 in a) #True
print(9 in a) #False 
print(2 not in a) #False
print(9 not in a ) #True
print("a" in b) #True
print()

#7-identity operators
n=4
m=8
c="ram"
print(n is m)
print()