def jumlah_kata(kata):
    kata = kata.title()
    # print(kata)
    list_kata = kata.split(' ')
    # print(list_kata)

    dict_kata = {}
    for itemList in list_kata:
        counter = 0
        for itemList2 in list_kata:
            if itemList == itemList2:
                counter += 1
        dict_kata[itemList] = counter
    
    # print(dict_kata)
    # print(dict_kata.keys())
    # print(dict_kata.values())

    for i,j in zip(dict_kata.keys(), dict_kata.values()):
        print("Jumlah kata '{}' ada sebanyak {}".format(i,j))

# kata = 'Aku baru makan nasi terus aku mau makan mie nanti malam'
kata = input('Masukkan string: \n')
# print(kata)
jumlah_kata(kata)
#contoh output:  Jumlah kata 'Aku' ada sebanyak 2