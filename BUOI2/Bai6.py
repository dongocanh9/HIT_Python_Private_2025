tong1=0
somon=0
while True :
    name=input("Nhập tên món : ")
    price=input("Nhập giá của món :")
    try:
        price=float(price)
    except ValueError:
        print("Giá nhập không hợp lệ, vui lòng nhập lại")
        continue
    s=input("Nhập pass để giữ món, skip để bỏ qua món, x hoặc X để thoát : ")
    if s=="pass":
        pass
    elif s=="skip":
        continue
    elif s=="x" or s=="X":
        break
    else:
        somon+=1
        tong1+=price
print(f"Tổng tiền trước giảm giá :{tong1} VND")
tong2=0
if tong1>200000 :
    giamgia=tong1*0.1
    tong2=tong1-giamgia
else:
    giamgia=0
    tong2=tong1
print(f"Số món đã gọi : {somon} món")
print(f"Giảm giá 10% : {giamgia} VND")
print(f"Tổng tiền phải trả : {tong2} VND")

