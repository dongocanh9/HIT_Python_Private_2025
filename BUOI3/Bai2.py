strings=input("Nhập vào chuỗi văn bản bất kì:")
chuoimoi=""
for char in strings:
    if char.isalpha() or char.isspace() :
        chuoimoi+=char
print(f"chuẩn hóa : {chuoimoi.lower()}")
nguyenam="ueoai"
strings_na=sum(1 for char in chuoimoi if char in nguyenam)
strings_pa=len(strings)-strings_na
print(f"Nguyên âm : {strings_na}")
print(f"Phụ âm : {strings_pa}")
b=chuoimoi.split( )
c=''.split( )
for char in b:
   d=char[::-1]
   c.append(d)
print(f"Đảo từng từ :{c}")
if strings==strings[::-1]:
   print("Palindrome : True")
else:
    print("Palindrome: False ")










