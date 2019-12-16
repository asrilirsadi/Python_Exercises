import math

hari = input('Masukkan jumlah hari : ')
hari = int(hari)
tahun = math.floor(hari/360)
bulan = math.floor((hari%360)/30)
minggu = math.floor(((hari%360)%30)/7)
hari = math.floor(((hari%360)%30)%7)
print(tahun, 'tahun ', bulan, 'bulan ', minggu, 'minggu ', hari, 'hari')