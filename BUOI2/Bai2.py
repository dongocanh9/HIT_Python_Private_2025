n=int(input("Nhập vào 1 số nguyên dương bất kì : "))
count=0
for i in range (2,n):
    if i**0.5==int(i**0.5):
        count+=1
print(count)
