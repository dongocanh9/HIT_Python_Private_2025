# Bài 2: Viết chương trình đếm số lượng mỗi chữ cái xuất hiện trong một từ.
#  Kết quả trả về dưới dạng dictionary, trong đó key là chữ cái và value là số lần xuất hiện.
# Input: Một từ (chỉ chứa các ký tự chữ cái a–z hoặc A–Z).


# Output: Một dictionary đếm số lần xuất hiện của từng chữ cái.
# Note: khi đếm không phân biệt in hoa in thường. 
# Ví dụ:
# Input:  “Happiness23424h”
# Output: {'h': 2, 'a': 1, 'p': 2, 'i': 1, 'n': 1, 'e': 1, 's': 2}
s=input("Nhập các chữ cái  chỉ chứa các ký tự a-z hoặc A-Z:")
for i in s:
    b=s.count(i)
    print(set(f"{i} : {b}",end=" "))  
