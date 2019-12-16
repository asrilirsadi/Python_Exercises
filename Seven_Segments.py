# print('#Solve it! 1')
listStr = ['Merdeka', 'Hello', 'Hellos', 'Sohib', 'Kari Ayam']
print(listStr)
searchItem = input('Search: ')
searchItem.lower()
listLower = list(map(lambda x: x.lower(), listStr))
# print(listLower)
listFilter = list(filter(lambda x: searchItem in x, listLower))
print(listFilter)

print('###---Seven Segments---###')
def numPool(splitNum, tempList1):
    Num0 = ['  __ ',' |  |',' |__|']
    Num1 = ['     ','    |','    |']
    Num2 = ['  __ ','  __|',' |__ ']
    Num3 = ['  __ ','  __|','  __|']
    Num4 = ['     ',' |__|','    |']
    Num5 = ['  __ ',' |__ ','  __|']
    Num6 = ['  __ ',' |__ ',' |__|']
    Num7 = ['  __ ','    |','    |']
    Num8 = ['  __ ',' |__|',' |__|']
    Num9 = ['  __ ',' |__|','  __|']
    
    for i in splitNum:
        if i == '0':
            tempList1.append(Num0)  
        elif i == '1':
            tempList1.append(Num1)      
        elif i == '2':
            tempList1.append(Num2) 
        elif i == '3':
            tempList1.append(Num3) 
        elif i == '4':
            tempList1.append(Num4) 
        elif i == '5':
            tempList1.append(Num5) 
        elif i == '6':
            tempList1.append(Num6) 
        elif i == '7':
            tempList1.append(Num7) 
        elif i == '8':
            tempList1.append(Num8) 
        elif i == '9':
            tempList1.append(Num9) 
    
    return tempList1

InputNum = input('Masukkan angka-angka: ')
splitNum = InputNum.split()
tempStr = ''
tempList1 = []
strTop = ''
strMid = ''
strBottom = ''

result1 = numPool(splitNum, tempList1)

for item in result1:
    for i in range(len(item)):
        if i == 0:
            strTop += item[i]
        elif i == 1:
            strMid += item[i]
        elif i == 2:
            strBottom += item[i]

print(strTop)
print(strMid)
print(strBottom)
            