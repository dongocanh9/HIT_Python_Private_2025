# 🧩 BÀI 1 — Quản lý điểm học sinh
# -------------------------------------------------------------
# Yêu cầu:
# 1. Cho danh sách điểm học sinh dưới dạng dict:
#    {"An": 8.5, "Bình": 7.2, "Chi": 9.0, "Dũng": 6.8, "Hà": 8.0}
# 2. Viết chương trình thực hiện các yêu cầu sau:
#    - In danh sách học sinh và điểm của họ.
#    - Tìm học sinh có điểm cao nhất và thấp nhất.
#    - Tính điểm trung bình của cả lớp.
#    - Tạo một dict mới lưu xếp loại (>=8: "Giỏi", 6.5–7.9: "Khá", <6.5: "Trung bình").
#    - Sắp xếp danh sách học sinh theo điểm giảm dần.
s= {"An": 8.5, "Bình": 7.2, "Chi": 9.0, "Dũng": 6.8, "Hà": 8.0}
print(s)
list1=[]
for values in s.values():
    list1.append(values)
print(list1)
