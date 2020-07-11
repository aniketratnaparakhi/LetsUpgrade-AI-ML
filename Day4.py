# Research on whether addition, subtraction, multiplication, division, floor division and modulo
# operations be performed on complex numbers. Based on your study, implement a Python
# program to demonstrate these operations.


A = complex(4,8)
B = complex(2,7)
print("copmlex num= ",A,B)
print("Addition of comp =",A+B)
print("Multiplication of comp =",A*B)
print("Sbubstraction of comp =",A-B)
print("Division of comp =",A/B)
# print("Floor Division of comp =",(A//B))
print("Modulo of comp =",abs(A))


# Research on range() functions and its parameters. Create a markdown cell and write in your own
# words (no copy-paste from google please) what you understand about it. Implement a small
# program of your choice on the same.

"""The range() function returns a sequence of numbers, starting from 0 by default,
 and increments by 1 ,by default, and stops before a specified number.
 in this example range function use for range start for 1 and ends of 8"""

x = range(1, 8)
for n in x:
  print(n)

# in this example range function use for range start for 2 and ends of 20 but it incremented by 2

y = range(2, 20, 2)
for n in y:
  print(n)

# Consider two numbers. Perform their subtraction and if the result of subtraction is greater than
# 25, print their multiplication result else print their division result.

Num1 = int(input("Enter the Number =\n"))
Num2 = int(input("Enter the Number =\n"))
Num3 = Num1 - Num2
if Num3 >= 25:
    print(Num1 * Num2)
else:
    print(Num1 / Num2)

# Consider a list of 10 elements of integer values. If the number in the list is divisible by 2, print the
# result as "square of that number minus 2"

list1 =[10,20,17,40,13,60,19,80,90,25]
print(list1)
for i in list1:
    if i%2==0:
        print(i*i-2)
    else:
        pass

# Consider a list of 10 elements. Print all the elements in the list which are greater than 7 when that
# number is divided 2.

list2 =[1,20,7,4,13,6,19,80,90,25]
for i in list2:
    if i >= 7:
        print(i/2)
    else:
        pass

