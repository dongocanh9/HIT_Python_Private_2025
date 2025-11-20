
s=input("Nhập các chữ cái  chỉ chứa các ký tự a-z hoặc A-Z:")
for i in s:
    b=s.count(i)
    print(f"{i} : {b}",end=" ")
