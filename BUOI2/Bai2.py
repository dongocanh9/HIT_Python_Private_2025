n=int(input("Nhập vào 1 số nguyên dương bất kì : "))
count=0
for n in range (2,n):
    if n**0.5==int(n**0.5):
        count+=1
print(count)