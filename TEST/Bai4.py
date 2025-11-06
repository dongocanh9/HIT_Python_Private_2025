# Bài 4: Tìm đoạn con dài nhất có các phần tử không trùng nhau
# Người dùng nhập vào một dãy số nguyên (cách nhau bởi dấu cách):
# Ví dụ nhập:
# 5 1 3 5 2 3 4 1
# Yêu cầu:
# Chuyển chuỗi thành list số nguyên.
# Tìm đoạn con liên tiếp dài nhất (subarray) mà không có phần tử nào lặp lại.
# In ra:
# Độ dài đoạn dài nhất
# Chính đoạn con đó (dạng tuple)
n=map(int,input("Nhập vào 1 dãy số nguyên cách nhau bởi dấu cách  :").split())
b=list(n)
print(b)
set1=set()
for i in b:
    if i not in set1:
        set1.add(i)
print(tuple(set1))

