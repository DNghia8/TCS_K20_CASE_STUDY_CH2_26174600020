ma_phien = input()
ma_may = input()
cong_suat_w = int(input())
so_phut = int(input())
don_gia = int(input())

dien_nang_tieu_thu = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_tieu_thu * don_gia

print(f"Ma phien: {ma_phien}")
print(f"May: {ma_may}")
print(f"Dien nang: {dien_nang_tieu_thu}")
print(f"Chi phi: {chi_phi}")
