def moveZeros(list):
    result_list = []
    zero_counter = 0
    # len_list
    for item in list:
        if type(item)==bool:
            result_list.append(item)
        elif item == 0:
            zero_counter += 1
        else: 
            result_list.append(item)
    # print(result_list)

    for i in range(zero_counter):
        result_list.append(0)

    print(result_list)
               
moveZeros([False,1,0,1,2,0,1,3,"a"])
moveZeros([0,0,0,"Test",0,3,"a",True])
moveZeros([True,True,False,"a","b",1,1,1])