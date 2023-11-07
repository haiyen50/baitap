diem_TB = eval(input("Nhập điểm trung bình"))
if diem_TB >=0 and diem_TB<=10:
    if diem_TB < 5:
        print("Yếu/kém")
    elif diem_TB <6:
        print("Trung bình")
    elif diem_TB <7:
        print("Trung bình/khá")
    elif diem_TB <8:
        print("Khá")
    elif diem_TB <9:
        print("Giỏi")
    else:
        print("Xuất sắc")
else:
    print("Nhập điểm không hợp lệ")