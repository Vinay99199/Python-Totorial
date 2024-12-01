#Operator precedece and associativity--------------------------------
#solve AKTU Question
a=3**2<<2>>5**2^10**3
b=3&5<<2//5**2+10^5
print(a) #1000
print(b) #5
print()

# implicit conversion-
a=3
b=3.5
c=a+b
print(c)  #6.5
print()

#explicit conversion-
a=3
b=3.5
c=a+b
print(int(b)) #3