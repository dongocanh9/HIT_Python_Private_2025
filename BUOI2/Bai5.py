while True:
    day=int(input("Nhập vào ngày sinh của bạn :"))
    month=int(input("Nhập vào tháng sinh của bạn :"))
    s=""
    if (day==20 and month>=1) or (day<=18 and month==2):
        s="Bảo Bình (Aquarius)"
    elif (day==19 and month>=2) or (day<=20 and month==3):
        s="Song Ngư (Pisces)"               
    elif (day==21 and month>=3) or (day<=19 and month==4):
        s="Bạch Dương (Aries)"
    elif (day==20 and month>=4) or (day<=20 and month==5):
        s="Kim Ngưu (Taurus)"
    elif (day==21 and month>=5) or (day<=21 and month==6):
        s="Song Tử (Gemini)"
    elif (day==22 and month>=6) or (day<=22 and month==7):
        s="Cự Giải (Cancer)"
    elif (day==23 and month>=7) or (day<=22 and month==8):
        s="Sư Tử (Leo)"
    elif (day==23 and month>=8) or (day<=22 and month==9):
        s="Xử Nữ (Virgo)"
    elif (day==23 and month>=9) or (day<=23 and month==10):
        s="Thiên Bình (Libra)"
    elif (day==24 and month>=10) or (day<=21 and month==11):
        s="Bọ Cạp (Scorpio)"
    elif (day==22 and month>=11) or (day<=21 and month==12):
        s="Nhân Mã (Sagittarius)"
    elif (day==22 and month>=12) or (day<=19 and month==1):
        s="Ma Kết (Capricorn)"
    else:
        s="Ngày hoặc tháng không hợp lệ !"
    print(f"Cung hoàng đạo của bạn :{s}")
    m=input("Bạn có muốn tiếp tục không (y/n) ? :")
    if m == "y"or m =="Y" :
        pass
    else:
        print("Kết thúc ")
        break


   
      

