ma_may = input()
print(type(ma_may))
cong_suat_w = input()
print(type(cong_suat_w))
so_phut_su_dung = input()
print(type(so_phut_su_dung))
gia_dien = input()
print(type(gia_dien))

dien_nang = float(cong_suat_w)*int(so_phut_su_dung)/60 / 1000
chi_phi = dien_nang * float(gia_dien)
print(f"Dien nang: {dien_nang}")
print(f"Chi phi: {chi_phi}")