cong_suat_w = int(input())
so_phut = int(input())
don_gia_kwh = int(input())

dien_nang_tieu_thu = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_tieu_thu * don_gia_kwh

print(dien_nang_tieu_thu," ", type(dien_nang_tieu_thu)) #ket_qua: 0.375 <class 'float'>
print(chi_phi," ", type(chi_phi)) #ket_qua: 1125.0 <class 'float'>

"""Sau khi thay so_phut = 60 thi dien nang tieu thu chi con 0.25 va chi phi la 750.0 nho hon so voi so_phut bang 90"""