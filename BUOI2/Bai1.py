import math
#1.2
n=int(input("Nhập váo 1 số nguyên bất kì : "))
tong=1
for n in range(2,n+1):
    tong+=1/math.factorial(n)
print(tong)
#1.1
tong=1
x=int(input("Nhập vào số nguyên x bất kì: "))
for n in range (2,n+1):
    giaithua=(1/math.factorial(n))*(x**n)
    tong+=giaithua
print(tong)
