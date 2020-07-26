
# Create a 3x3x3 array with random values
import numpy as np
print(" 1.Create a 3x3x3 array with random values =\n")
x = np.random.random((3,3,3))
print(x)

# 2.Create a 5x5 matrix with values 1,2,3,4 just below the diagonal"
print("2.Create a 5x5 matrix with values 1,2,3,4 just below the diagonal=\n")
y = np.diag([1,2,3,4,5])
print(y)

# 3.Create a 8x8 matrix and fill it with a checkerboard pattern"

print("3.Create a 8x8 matrix and fill it with a checkerboard pattern=\n")
z = np.zeros((8,8),dtype=int)
z[1::2, ::2] = 1
z[::2, 1::2] = 1
print(z)

# 4. Normalize a 5x5 random matrix"
print("4. Normalize a 5x5 random matrix =\n")
a = np.random.random((5,5))
print("original =", + a ,"\n")
amax, amin = a.max(), a.min()

a = (a - amin)/(amax - amin)

print("normalize= ", + a)

# 5.  How to find common values between two arrays?"
print("5.  How to find common values between two arrays\n?")
arr1 = np.array([10,20,30,40,50])
arr2 = np.array([12,45,78,40,20])
print("array1 =", arr1, "\n" "array2 =",arr2)

print("common value = ",np.intersect1d(arr1, arr2))


# 6.How to get the dates of yesterday, today and tomorrow?"
print("6.How to get the dates of yesterday, today and tomorrow?=\n")
yesterday = np.datetime64('today','D') - np.timedelta64(1,'D')
print("yesterday =", yesterday)
today = np.datetime64('today','D')
print("today =", today)
tomorrow = np.datetime64('today','D') + np.timedelta64(1,'D')
print("tomorrow =",tomorrow)

# 7. Consider two random array A and B, check if they are equal"
print("7. Consider two random array A and B, check if they are equal\n")
a1 = np.random.randint(1,2,3)
a2 = np.random.randint(1,2,3)

B =np.allclose(a1, a2)
print(B)

# 8.Create random vector of size 10 and replace the maximum value by 0
print("8.Create random vector of size 10 and replace the maximum value by 0 \n")
c = np.random.random(10)
print(c)
c[c.argmax()] = 0
print("maximum value replace by 0",c)

# 9. How to print all the values of an array?"
print("9. How to print all the values of an array?=\n")
v = np.zeros((4,4))
print(v)

# 10.Subtract the mean of each row of a matrix"
print("10.Subtract the mean of each row of a matrix=\n")
n = np.random.rand(5,10)
print("original matrix= ",n)
m = n - n.mean(axis=1, keepdims=True)
print("Subtract the mean of each row",m)

# 11.Consider a given vector, how to add 1 to each element indexed by a second vector (be careful with repeated indices)
vetr = np.array([1,2,3,4,5])

# 12.How to get the diagonal of a dot product?"
print("12.How to get the diagonal of a dot product?=\n")

p1 = np.random.randint(0,10,(3,3))
z1 = np.random.randint(0,10,(3,3))
print("first array",p1)
print("second array",z1)
p2 = np.diag(p1)
print("daigonal of 1st array",p2)
z2 = np.diag(z1)
print("daigonal of 2nd array",z2)
print("dot product of both daigonal array",p2.dot(z2))

# 13.How to find the most frequent value in an array?"
print("13.How to find the most frequent value in an array?=\n")
x1 = np.random.randint(0,10,40)
print("original array",x1)
print("most frequent value =",np.bincount(x1).argmax())

# 14.How to get the n largest values of an array"
print("14.How to get the n largest values of an array=\n")
arr3 = np.array([10,30,20,12,3,50])
print("array=",arr3)
max = arr3[0]

for i in range(0,len(arr3)):
    if(arr3[i]>max):
        max = arr3[i]
print("largest value in array=",max)

# 15.How to create a record array from a regular array?"
print("15.How to create a record array from a regular array?=\n")
b1 = np.array([1,2,3])
b2 = np.array(['Red','Green','Blue'])
b3 = np.array([10.3,20,50])
result = np.core.records.fromarrays([b1,b2,b3],names='a,b,c')
print(result[0])
print(result[1])
print(result[2])
