import random
class ramalan:
    def __init__(self, harga, pilihan = 0):
        self.cost = harga
        self.pilih = pilihan
        self.ramalan1 = {1: 'Menganggur', 
                         2: 'Kerja gajinya kecil', 
                         3: 'Kerja cukup nyaman', 
                         4: 'Kerja gajinya besar tapi ga nyaman', 
                         5: 'Kerja gajinya besar dan nyaman'}
        self.ramalan2 = {1: 'Terkena sakit kronis', 
                         2: 'Gejala sakit kronis', 
                         3: 'Badan lemes', 
                         4: 'Terserang Flu, Demam', 
                         5: 'Sehat Jasmani Rohani'}
        self.ramalan3 = {1: 'Jomblo seumur hidup', 
                         2: 'Nembak gebetan ditolak', 
                         3: 'Dapet Pacar', 
                         4: 'Menikah dengan pasangan idaman', 
                         5: 'Menikah dan hidup bahagia selamanya'}
        
    def result_ramalan(self):
        list_Ramalan = {}
        list_Prob = []
        if self.pilih == 1:
            list_Ramalan = self.ramalan1
        elif self.pilih == 2:
            list_Ramalan = self.ramalan2
        elif self.pilih == 3:
            list_Ramalan = self.ramalan3
        
        if self.cost > 10000 and self.cost < 50000:
            for i in range(80):
                list_Prob.append(list_Ramalan[random.randint(3, 5)])
            for i in range(10):
                list_Prob.append(list_Ramalan[2])
            for i in range(10):
                list_Prob.append(list_Ramalan[1])
        elif self.cost == 10000:
            for i in range(10):
                list_Prob.append(list_Ramalan[5])
            for i in range(80):
                list_Prob.append(list_Ramalan[random.randint(2, 4)])
            for i in range(10):
                list_Prob.append(list_Ramalan[1])
        elif self.cost < 10000:
            for i in range(10):
                list_Prob.append(list_Ramalan[5])
            for i in range(10):
                list_Prob.append(list_Ramalan[4])
            for i in range(80):
                list_Prob.append(list_Ramalan[random.randint(1, 3)])
        print('\n Hasil Ramalan: ' + list_Prob[random.randint(0,99)])

    def menu(self):
        print('\nPilih ramalan Anda: \n1. Ramalan Pekerjaan \n2. Ramalan Kesehatan \n3. Ramalan Percintaan \n4. Keluar')
        pilihan = int(input('Masukkan Pilihan: '))
        if pilihan > 0 and pilihan < 4:
            self.pilih = pilihan
            self.result_ramalan()
        elif pilihan == 4:
            print('Terima Kasih')

Asril = ramalan(15000)
Asril.menu()