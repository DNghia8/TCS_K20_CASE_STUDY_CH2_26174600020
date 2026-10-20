tong_phut = 135
cong_suat_w = 250

so_gio_tron_ven = tong_phut//60
so_phut_con_lai = tong_phut%60
print(so_gio_tron_ven)
print(so_phut_con_lai)

su_dung_lau = False
du_lieu_hop_le = False

if(tong_phut>60):
    su_dung_lau = True
if(cong_suat_w > 0 and tong_phut>0):
    du_lieu_hop_le = True
print(su_dung_lau)
print(du_lieu_hop_le)

print(100+20*3) # Ket qua: 160
print((100+20)*3) # Ket qua: 360