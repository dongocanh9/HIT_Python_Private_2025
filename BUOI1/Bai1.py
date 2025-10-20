#Bài 1 :
a,b=map(int,input("Nhập 2 số a , b bất kì ").split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a**b)
print(a%b)
if a>b :
    print("a lớn hơnb")
elif a <b:
    print("a nhỏ hơn b")
else : 
    print("a bằng b ")
print(a & b)
print(a / b)
print(a^b)
n=bin(a)[2:]
print(n[::-1])
