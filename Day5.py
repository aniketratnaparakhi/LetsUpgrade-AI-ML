# Write a Python program to find the first 20 non-even prime natural numbers.
A = int(input("Enter  Range: "))
B = int(input("Enter  Range: "))
print("Prime numbers between", A, "and", B, "are:")
for num in range(A, B + 1):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)

# Write a Python program to implement 15 functions of string.

str1 = "Aniket"
str2 = "Ratnaparakhi"
str = "java"
print(len(str1))
print(len(str2))
print(slice(str1,str2))
print(str1[2:4])
print(str1.upper())
print(str2.lower())
print(",".join(str1))
str3 = str.replace('java','python is great')
print(str3)
print(str3.find('py'))
print(str3.count('python'))
print(str3.endswith('great'))
print(str1.center(10))
print(str1.expandtabs())
print(str1.rjust(60))
print(str3.strip('py'))
print(ascii(str1))


# Write a Python program to check if the given string is a Palindrome or Anagram or None of them.
# Display the message accordingly to the user.


s1=input(("Enter a string:= \n"))
s2=input(("Enter a string:= \n"))


if(sorted(s1)== sorted(s2)):
    print("The strings are anagrams.")
else:
    print("The strings aren't anagrams.")

if (s1 == s1[::-1]):
    print("The string is a palindrome")
else:
    print("Not a palindrome")

# Write a Python's user defined function that removes all the additional characters from the string
# and converts it finally to lower case using built-in lower(). eg: If the string is "Dr. Darshan Ingle
# @AI-ML Trainer", then the output be "drdarshaningleaimltrainer".


original_string = "Dr. Darshan Ingle@AI-ML Trainer"
characters_to_remove = ". @ - "

new_string = original_string
for character in characters_to_remove:
  new_string = new_string.replace(character, "")

print(new_string.lower())