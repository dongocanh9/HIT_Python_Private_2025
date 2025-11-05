s=input("Nhập vào 1 đoạn văn bản : ")
s1=s.lower()
words=s1.split()
print(words)
s2=[]
for char in words :
    if char not in s2:
        s2.append(char)
print(s2) 
counts=[]
for char in s2:
    b=words.count(char)
    counts.append(b)
    print(f"Từ {char} xuất hiện {b} lần ")
for  char in s2:
    b=words.count(char)
    if b==max(counts):
        print("Từ xuất hiện nhiều nhất : ", char)
a=max(s2,key=len)
print("Từ có độ dài dài nhất : " , a)
tong=sum(len(char) for char in words)
print("Tổng số kí tự : ",tong)
listmoi=[]
while s2:
    a = max(s2,key=len) 
    s2.remove(a)           
    listmoi.append(a)      
print(f"Sắp xếp theo độ dài giảm dần: {listmoi}")



