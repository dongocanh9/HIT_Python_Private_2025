import re
email=input("Nhập vào địa chỉ email của bạn : ")
pattern = r'^\w+@\w+\.\w+$'
if re.match(pattern,email):
    print("Vaild")
else:
    print("Invalid")
    