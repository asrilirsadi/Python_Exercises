def get_highest_xnum(num, sequence):
    str_num = str(num)
    max_seq_num = 0
    if len(str_num)<=10 and sequence>=2 and sequence<=5:
        for i in range(len(str_num)-sequence+1):
            if int(str_num[i:sequence+i]) > max_seq_num:
                max_seq_num = int(str_num[i:sequence+i])
    print(max_seq_num)

get_highest_xnum(1794103177,3)
get_highest_xnum(1794103177,4)
get_highest_xnum(87173114,5)