import math
#1.2
n=int(input("Nhập váo 1 số nguyên không âm bất kì : "))
S=1
for i in range(2,n+1):
    S+=1/math.factorial(i)
print(S)
#1.1
tong=1
x=int(input("Nhập vào số nguyên x bất kì: "))
n=int(input("Nhập váo 1 số nguyên không âm bất kì : "))
for i in range (2,n+1):
    giaithua=(1/math.factorial(i))*(x**i)
    tong+=giaithua
print(tong)
