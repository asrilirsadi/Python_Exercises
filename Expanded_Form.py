# import math
# def expandedForm(num):
#     start = len(str(num)) - 1
#     z = ''
#     for i in range(start, -1, -1):
#         power = 10**i
#         itemNum = int(num/power)*power
#         if itemNum != 0:
#             num = num - itemNum
#             z += str(itemNum) + ' + '
#     print(z[:-2])

# expandedForm(703)

#CARA LAIN
def expanded_form(nomor):
    from math import floor, pow
    angka = []
    while (nomor > 0):
        angka.append(nomor%10)
        nomor = floor(nomor/10)
    # print(angka)
    for idx, val in enumerate(angka):
        angka[idx] = int(val * pow(10, idx))
    # print(angka)
    z = ''
    for idx in range(len(angka)-1,-1,-1):
        if angka[idx] != 0 and idx !=0:
            z += str(angka[idx])
            z += ' + '
        elif angka[idx] != 0 and idx == 0:
            z += str(angka[idx])
    print(z)
expanded_form(703)
