#Bài 2.
# s=input("Nhập vào 1 chuỗi ký tự ")
# if "hit" in s or "HIT" in s : 
#     print("True")
# else:
#     prinṭ̣̣("False")
# if "16" not in s :
#     print("True")
# else:
#     print("False")
CREATE DATABASE QLSV;
GO

USE QLSV;
GO

CREATE TABLE KHOA (
    MaKhoa    VARCHAR(10) PRIMARY KEY,
    TenKhoa   NVARCHAR(50) NOT NULL,
    DienThoai VARCHAR(15)
);

CREATE TABLE LOP (
    MaLop     VARCHAR(10) PRIMARY KEY,
    TenLop    NVARCHAR(50) NOT NULL,
    KhoaHoc   INT,
    HeDaoTao  NVARCHAR(30),
    NamNhapHoc INT,
    MaKhoa    VARCHAR(10) NOT NULL,
    FOREIGN KEY (MaKhoa) REFERENCES KHOA(MaKhoa)
);

CREATE TABLE SINHVIEN (
    MaSV      VARCHAR(10) PRIMARY KEY,
    HoDem     NVARCHAR(30) NOT NULL,
    Ten       NVARCHAR(15) NOT NULL,
    Que       NVARCHAR(50),
    GioiTinh  NVARCHAR(5),
    NgaySinh  DATE,
    MaLop     VARCHAR(10) NOT NULL,
    FOREIGN KEY (MaLop) REFERENCES LOP(MaLop)
);

CREATE TABLE MONHOC (
    MaMH      VARCHAR(10) PRIMARY KEY,
    TenMonHoc NVARCHAR(50) NOT NULL,
    SoDVHT    INT
);

CREATE TABLE DIEMTHI (
    MaSV      VARCHAR(10) NOT NULL,
    MaMonHoc  VARCHAR(10) NOT NULL,
    LanThi    INT NOT NULL,
    DiemLan1  DECIMAL(4, 2),
    PRIMARY KEY (MaSV, MaMonHoc, LanThi),
    FOREIGN KEY (MaSV) REFERENCES SINHVIEN(MaSV),
    FOREIGN KEY (MaMonHoc) REFERENCES MONHOC(MaMH)
);
USE QLSV;
GO

INSERT INTO KHOA (MaKhoa, TenKhoa, DienThoai) VALUES
('CNTT', N'Công nghệ Thông tin', '02438685121'),
('KT', N'Kinh tế', '02438685122'),
('CK', N'Cơ khí', '02438685123');

INSERT INTO LOP (MaLop, TenLop, KhoaHoc, HeDaoTao, NamNhapHoc, MaKhoa) VALUES
('K65_CNPM', N'CNPM K65', 65, N'Đại học Chính quy', 2023, 'CNTT'),
('K64_ATTT', N'ATTT K64', 64, N'Đại học Chính quy', 2022, 'CNTT'),
('K65_QLKT', N'Quản lý Kinh tế K65', 65, N'Đại học Chính quy', 2023, 'KT');

INSERT INTO SINHVIEN (MaSV, HoDem, Ten, Que, GioiTinh, NgaySinh, MaLop) VALUES
('SV001', N'Nguyễn Văn', N'A', N'Hà Nội', N'Nam', '2005-01-15', 'K65_CNPM'),
('SV002', N'Trần Thị', N'B', N'Hải Phòng', N'Nữ', '2004-11-20', 'K65_CNPM'),
('SV003', N'Lê Văn', N'C', N'Nam Định', N'Nam', '2004-05-10', 'K64_ATTT'),
('SV004', N'Phạm Thu', N'D', N'Thanh Hóa', N'Nữ', '2005-03-25', 'K65_QLKT');

INSERT INTO MONHOC (MaMH, TenMonHoc, SoDVHT) VALUES
('CSDL', N'Cơ sở Dữ liệu', 3),
('MMT', N'Mạng Máy tính', 3),
('TC01', N'Tài chính Doanh nghiệp', 4),
('GT01', N'Giải tích 1', 3);

INSERT INTO DIEMTHI (MaSV, MaMonHoc, LanThi, DiemLan1) VALUES
('SV001', 'CSDL', 1, 8.50),
('SV001', 'GT01', 1, 7.00),
('SV002', 'CSDL', 1, 5.00),
('SV002', 'CSDL', 2, 7.25),
('SV002', 'MMT', 1, 9.00),
('SV003', 'CSDL', 1, 6.00),
('SV003', 'MMT', 1, 8);

SELECT * FROM KHOA;
SELECT * FROM LOP;
SELECT * FROM SINHVIEN;
SELECT * FROM MONHOC;
SELECT * FROM DIEMTHI;

