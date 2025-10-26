n=int(input("Nhập vào số lượng học viên :"))
for i in range(1,n+1):
    hoten=input("Nhập vào họ tên học viên :")
    diem1=int(input("Nhập vào điểm bài kiểm tra thứ nhất :"))
    diem2=int(input("Nhập vào điểm bài kiểm tra thứ hai :"))
    tongdiem=diem1+diem2
    print(f"{i} {hoten} {tongdiem}{' Xuất sắc' if tongdiem>=200 else ' Giỏi' if 150<=tongdiem<200 else ' Khá' if 100<=tongdiem<150 else'Yếu'}")
