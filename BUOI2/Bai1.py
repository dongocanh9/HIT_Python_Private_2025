import math
#1.2
n=int(input("Nhập váo 1 số nguyên không âm bất kì : "))
S=1
for n in range(2,n+1):
    S+=1/math.factorial(n)
print(S)
#1.1
e^x=1
x=int(input("Nhập vào số nguyên x bất kì: "))
n=int(input("Nhập váo 1 số nguyên không âm bất kì : "))
for n in range (2,n+1):
    giaithua=(1/math.factorial(n))*(x**n)
    e^x+=giaithua
print(e^x)
