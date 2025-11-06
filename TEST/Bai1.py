# Bài 1. Quản lý kho hàng

# Một chuỗi nhập vào chứa danh sách hàng hoá theo dạng:
# Ví dụ: "TV, Laptop, Phone, TV, Tablet, Laptop, Camera"

# Hãy viết chương trình:
# 1. Chuyển chuỗi thành list.
# 2. Loại bỏ trùng lặp bằng set, sau đó chuyển lại thành tuple. In ra tuple (Hiển thị danh sách hàng hoá duy nhất)
# 3. Đếm số loại hàng hoá (len() tuple) và in ra số loại hàng hóa
# 4. Có 3 sản phẩm bán chạy là : {"Phone", "Laptop", "Smartwatch"}.
# 5. In ra danh sách loại sản phẩm có trong kho và bán chạy (intersection).
# 6. In ra loại sản phẩm chỉ có trong kho nhưng không bán chạy (difference).
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


