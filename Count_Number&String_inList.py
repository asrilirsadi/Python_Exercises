StrNumList = [3,1,'a','5',9,'1','A',5,4,'A','B','1',2,3,'a',5,'B','A']

def countProcess(arr):
    arrTemp = arr
    dict_arr = {}
    
    for item in arrTemp:
        counter = 0
        list_val = ['',0]
        for item2 in arrTemp:
            if item == item2:
                counter += 1
        if type(item) == str:
            list_val[0] = 'string'
        elif type(item) == int:
            list_val[0] = 'integer'
        elif type(item) == float:
            list_val[0] = 'float'
        list_val[1] = counter
        dict_arr[item] = list_val

    for i,j in zip(dict_arr.keys(), dict_arr.values()):
        print('{} {} ada {} karakter'.format(i, j[0], j[1]))

countProcess(StrNumList)

# print(type('a'))
# print(type(2) == int)
# print(type(3.1))
# print(type('w') == str)
print(type(True))

