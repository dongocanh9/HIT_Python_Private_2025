s="An:8.5, Binh:7.0, An:9.0, Cuong:6.5, Binh:8.0, Dung:7.5"
a=s.split(',')
listmoi=[]
set1={}
for i in a :
    ten , diem= i.strip().split(':')
    diem1=float(diem)
    listmoi.append((ten,diem1))
print(listmoi)
set1=set()
for i in  listmoi:
    b=i[0]
    if b not in set1:
        set1.add(b)
print(set1)
list2=[]
for ten in set1:
    list1=[]
    for i in listmoi:
        if i[0]==ten:
            list1.append(i[1])
    list2.append(sum(list1)/len(list1))
    print(f"{ten} : {sum(list1)/len(list1)}")
print(list2)
mins =[ten for ten, i in zip(set1, list2) if i == min(list2)]
maxs=[ten for ten, i in zip(set1, list2) if i == max(list2)]
print("Sinh viên cao nhất :",*mins)
print("Sinh viên thấp nhất :",*maxs)
list3=list(zip(set1,list2))
for i in range (len(list3)):
    for j in range (i+1,len(list3)):
        if list3[0][1]<list3[0][1]:
            list3[i],list3[i]=list3[j],list3[j]
print(tuple(list3))

   






   