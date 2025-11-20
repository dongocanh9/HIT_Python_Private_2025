s="TV, Laptop, Phone, TV, Tablet, Laptop, Camera"
s1=list(s.strip().split(","))
print(s1)
set1=set(s1[0:3])
set2=set(s1[3:])
set3=set1.union(set2)
print(tuple(set3))
list1=list(set3)
print(list1)
for i in list1:
    b=list1.count(i)
    print(f"hàng hóa {i} xuất hiện {b} lần")
banchay={" Phone", " Laptop", " Smartwatch"}
a=banchay.intersection(set3)
print(a)
b=set3.difference(banchay)
print(b)


