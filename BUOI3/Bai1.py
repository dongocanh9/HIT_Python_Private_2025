numbers = list(map(int,input("Nhập các số nguyên cách nhau bởi dấu phẩy ").split(',')))
#Cách 1(câu1)
list1=numbers[0:3]
list2=numbers[3:]
set1=set(list1)
set2=set(list2)
setmoi=set1.union(set2)
listmoi=list(setmoi)
print(listmoi)
#Cách 2
list1=[]
for i in numbers:
    if i not in list1 :
        list1.append(i)
print(f"Sau khi loại trùng :{list1}")
#câu2
listmoi=[i**2 if i%2==0 else i**3 for i in list1]
print(f"List mới : {listmoi}")
#câu3
avg=[]
for i in list1 :
    b=list1.index(i)
    if b %2==0:
        avg.append(i)
    trungbinhcong=sum(avg)/len(avg)
print(f"Trung bình vị trí chẵn {trungbinhcong}")
#câu4
listc=[]
while list1 :
    a=min(list1, key=lambda x: abs(x))
    list1.remove(a)
    listc.append(a)
print(f"Sắp xếp theo abs : {listc}")





