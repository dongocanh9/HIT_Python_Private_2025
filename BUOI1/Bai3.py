s1 ='Chao mung den CLB Tin Hoc HIT'
print(s1.upper())
print(s1.lower())
print(s1.strip())
print(s1.title())
s2='CLB Tin hoc HIT truc thuoc Truong CNTT-"10 diem"'
print(s2.upper())
print(s2.lower())
print(s2.strip())
print(s2.title())
s3="CLB Tin Hoc HIT truc thuoc Truong CNTT"
for i in s3 :
    if i.isupper():
       print(i, end=" ")
print()      
for i in s3 :
    if i.islower():
        print(i,end=" ")
print()
if "CNTT" in s3 :
     print("Yes")
else :
    print("No")
s4="".join([i.upper() if i.islower()else i.lower() if i.isupper() else i for i in  s3])
print(s4)
print("THÔNG TIN HIT 16")
hoten=input(" Nhập họ và tên của cậu : ")
tuoi=int(input("Cậu mấy tuổi rùi nhỉ ? "))
gioitinh=input("Giới tính của cậu (Nam/Nữ) ?")
tinhtranghonnhan=input("Tình trạng hôn nhân của cậu ( Độc thân / Hẹn hò/ Kết hôn/Ly hôn/Khác) :")
print(hoten)
print(tuoi)
print(gioitinh)
print(tinhtranghonnhan)
print("Thông tin đã được in lên terminal của trường.Muốn có người iu vui lòng liên hệ ngay anh Hùng !!!")