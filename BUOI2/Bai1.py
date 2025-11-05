import math
#1.2
n=int(input("Nhập váo 1 số nguyên không âm bất kì : "))
S=1
<<<<<<< HEAD
for n in range(2,n+1):
    S+=1/math.factorial(n)
=======
for i in range(2,n+1):
    S+=1/math.factorial(i)
>>>>>>> a891e1267c3fd3173c88796cf1bc15fbdf582f22
print(S)
#1.1
tong=1
x=int(input("Nhập vào số nguyên x bất kì: "))
n=int(input("Nhập váo 1 số nguyên không âm bất kì : "))
<<<<<<< HEAD
for n in range (2,n+1):
    giaithua=(1/math.factorial(n))*(x**n)
=======
for i in range (2,n+1):
    giaithua=(1/math.factorial(i))*(x**i)
>>>>>>> a891e1267c3fd3173c88796cf1bc15fbdf582f22
    tong+=giaithua
print(tong)