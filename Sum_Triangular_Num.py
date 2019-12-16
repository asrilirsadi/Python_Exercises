n = int(input('Input: '))

def sum_triangular_num(n):
    z = ''
    sum = 0
    num = 0

    for i in range(n):
        for j in range(i+1):
            num += 1
            if j == i:
                z += '[{}]'.format(num)
                sum += num
            else:
                z += ' {}'.format(num)
            z += '\t'
        z += '\n\n'
    return z, sum

res1, res2 = sum_triangular_num(n)
print(res1)
print('sum of each last part of the triangle is {}'.format(res2))