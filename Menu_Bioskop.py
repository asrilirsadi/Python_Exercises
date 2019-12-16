history_pesanan = {}
transaksi = 0
logout = 0

def menu_bioskop(history_pesanan, transaksi):
    transaksi += 1
    logout = 0
    print('Menu :')
    print('1. Pesan Tiket')
    print('2. Lihat History')
    print('3. Keluar')
    Pilihan = input('Tentukan Pilihan: ')
    if Pilihan == '1':
        list_film(history_pesanan, transaksi)
    elif Pilihan == '2':
        transaksi -= 1
        history_transaksi(history_pesanan)
    elif Pilihan == '3':
        logout = 1
        return logout
    else:
        transaksi -= 1
        print('Mohon maaf pilihan yang Anda input tidak tersedia. Silahkan pilih menunya kembali: ')
        menu_bioskop(history_pesanan, transaksi)

def list_film(history_pesanan, transaksi):
    Film = ''
    print('\nList Film :')
    print('1. The Incredible')
    print('2. Toy Story')
    pilihFilm = input('Silahkan Pilih Film: ')
    if pilihFilm == '1':
        Film = 'The Incredible'
    elif pilihFilm == '2':
        Film = 'Toy Story'
    else:
        print('Mohon maaf pilihan yang anda input kurang tepat.')
        print('Silahkan pilih Film dengan menginput nomor pilihan Film yang tersedia:') 
        list_film(history_pesanan, transaksi)
    list_jadwal(Film, history_pesanan, transaksi)

def list_jadwal(Film, history_pesanan, transaksi):
    jadwal = ''
    print('\nPilih jadwal Film ' + Film + ' :')
    print('1. Siang')
    print('2. Malam')
    pilihJadwal = input('Pilihan : ')
    if pilihJadwal == '1':
        jadwal = 'Siang'
    elif pilihJadwal == '2':
        jadwal = 'Malam'
    else:
        print('Mohon maaf pilihan yang anda input kurang tepat.')
        print('Silahkan pilih Film dengan menginput nomor pilihan Film yang tersedia:') 
        list_jadwal(Film, history_pesanan, transaksi)
    jmlTiket = int(input('Pesan tiket berapa kali: '))
    for jmlTiket in range(jmlTiket):
        if jmlTiket > 0:
            transaksi += 1
        pesan_tiket(Film, jadwal, history_pesanan, transaksi)

def pesan_tiket(Film, jadwal, history_pesanan, transaksi):
    # jmlTiket = int(input('Pesan tiket berapa kali: '))
    row = int(input('Row : '))
    seat =  int(input('Seat : '))

    check = available_check(history_pesanan, Film, jadwal, row, seat)

    if check == 0:
        print('Mohon maaf kursi tidak tersedia')
        pesan_tiket(Film, jadwal, history_pesanan, transaksi)
    elif check == 1:
        # print('Kursi tersedia')
        history_pesanan[transaksi] = [Film, jadwal, row, seat]
        
    kursi_dipilih = pilih_kursi(history_pesanan, Film, jadwal)
    print(lihat_kursi(kursi_dipilih))

    # print('\n')
    menu_bioskop(history_pesanan, transaksi)

def available_check(history_pesanan, Film, jadwal, row, seat):
    val = 0

    if history_pesanan == {}:
        val = 1
    else:
        for item in zip(history_pesanan.values()):
            if (item[0][0] == Film) and (item[0][1] == jadwal) and (item[0][2] == row) and (item[0][3] == seat):
                val = 0
                break
            else:
                val = 1
    return val

def lihat_kursi(kursi_bioskop):
    z = ''
    for i in kursi_bioskop:
        for j in range(len(i)):
            z += '{}'.format(i[j])
        z += '\n'
    return z                 

def pilih_kursi(result, film, jadwal):
    kursi_bioskop = [['0','0','0','0','0','0','0','0','0','0'],
                     ['0','0','0','0','0','0','0','0','0','0'],
                     ['0','0','0','0','0','0','0','0','0','0'],
                     ['0','0','0','0','0','0','0','0','0','0'],
                     ['0','0','0','0','0','0','0','0','0','0']]
    kursi_tersedia = []
    
    for item in zip(result.values()):
        if (item[0][0] == film) and (item[0][1] == jadwal):
            kursi_tersedia.append([item[0][2], item[0][3]])
            
    for item2 in kursi_tersedia:
        row = item2[0]
        seat = item2[1]
        for i in range(len(kursi_bioskop)):
            for j in range(len(kursi_bioskop[i])):
                if (row-1) == i and (seat-1) == j:
                    kursi_bioskop[i][j] = 'X'
    return kursi_bioskop

def history_transaksi(history_pesanan):
    for i in zip(history_pesanan.values()):
        print("Film: {}, Jadwal: {}, Row: {}, Seat: {}".format(i[0][0], i[0][1], i[0][2], i[0][3])) 

    menu_bioskop(history_pesanan, transaksi)

# print(history_pesanan)
# print(transaksi)
logout = menu_bioskop(history_pesanan, transaksi)
if logout == 1:
    print('\nTerima Kasih')
