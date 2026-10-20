from datetime import datetime
thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")
print(thoi_diem)
print(type(thoi_diem))
print(thoi_diem_text)
print(type(thoi_diem_text))
bat_dau = datetime(2026, 10, 14, 13, 15)
ket_thuc = datetime(2026, 10, 14, 15, 5)
thoi_luong = ket_thuc - bat_dau
print(thoi_luong) #Ket qua: 1:50:00
print(type(thoi_luong))

#datetime: la chi moc thoi gian cu the trong may khi bat dau chay chuong trinh
#str: la bieu dien moc thoi gian cu the trong may khi bat dau duoi dang string
#timedelta: la khoang thoi gian chenh lech