class BikinMenu():
    def __init__(self, nama, menu, price, history = []):
        self.name = nama
        self.menulist = menu
        self.pricelist = price
        menu_Dict = {}
        if len(self.menulist) == len(self.pricelist):
            for i in range(len(self.menulist)):
                menu_Dict[self.menulist[i]] = self.pricelist[i]
        self.Menu_Dict = menu_Dict
        self.history_list = history

    def get_menu(self):
        print('Menu Makan\n')
        no = 0
        for i, j in zip(self.Menu_Dict.keys(), self.Menu_Dict.values()):
            no += 1
            print('{}. {} harganya adalah {}'.format(no, i, j))
    
    def menu_price(self):
        # menu_dict = menupriceList(self)
        pilih = int(input('Mau beli yang mana: '))
        self.history_list.append(pilih-1)
        for i in range(len(self.menulist)+1):
            if pilih == i:
                menupilihan = self.menulist[i-1]
                for i,j in zip(self.Menu_Dict.keys(), self.Menu_Dict.values()):
                    if menupilihan == i:
                        print('{} telah membeli {} dengan harga {}'.format(self.name, i, j))
    
    def get_history(self):
        len_history = len(self.history_list)
        # menu_history = []
        # str_print = '{} telah membeli '.format(self.name)

        if len_history == 0:
            print('Belum ada pembelian')
        else:
            str_print = '{} telah membeli '.format(self.name)
            for i in range(len(self.history_list)):
                    if i == 0:
                        str_print += self.menulist[self.history_list[i]]
                    elif i == len(self.history_list)-1:
                        str_print += ', dan {}.'.format(self.menulist[self.history_list[i]])
                    else:
                        str_print += ', {}'.format(self.menulist[self.history_list[i]])
        print(str_print)


Paul = BikinMenu('Paul', ['Ayam Goreng', 'Nasi Bakar', 'Sate Kambing'], [1000, 2000, 3000])

Paul.get_menu()

Paul.menu_price()
Paul.get_history()
Paul.menu_price()
Paul.get_history()
Paul.menu_price()
Paul.get_history()
Paul.menu_price()
Paul.get_history()