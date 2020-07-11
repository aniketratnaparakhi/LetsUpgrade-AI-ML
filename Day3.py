import math

#________________ Write a program to subtract two complex numbers in Python._________________

c = complex(2,3)
print("c =",c)

d = complex(4,-2)
print("d =",d)

print("complex number substraction=",c-d)

# ________________Write a program to find the fourth root of a number.________________________

a =int(input("Enter the Number of 4th root=\n"))
print(a**4)

# ________________Write a program to swap two numbers in Python with the help of a temporary variable__
x = 2
y = 3

temp= x
x = y
y= temp

print("after swapping =",x)
print("after swapping =",y)

# ________________Write a program to swap two numbers in Python without using a temporary variable.________
p = 4
q = 6
p,q = q,p
print("after swapping =",p)
print("after swapping =",q)

# Write a program to convert fahrenheit to kelvin and celsius both.

# ______________Write a program to demonstrate all the available data types in Python. Hint: Use type() function.
f1="Aniket"
print(f1,"type=",type(f1),"\n")
f2 = 123
print(f2,"type=",type(f2),"\n")
f3 = 143.45
print(f3,"type=",type(f3),"\n")
f4 = True
print(f4,"type=",type(f4),"\n")
f5 = complex(2,3)
print(f5,"type=",type(f5))

