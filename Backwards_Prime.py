def backwardPrimes(start,stop):
    result = []
    for i in range(start, stop+1):
        if i>9:
            checkPrime = check_Prime(i)
            if checkPrime == True:
                backward_Temp = str(i)[::-1]
                if str(i) != backward_Temp:
                    check_BackwardPrime = check_Prime(int(backward_Temp))
                    if check_BackwardPrime == True:
                        result.append(i)
    print(result)

def check_Prime(i):
    check = True
    for j in range(2, i):
        if i%j == 0:
            check = False
            break
        else:
            check = True
    return check

backwardPrimes(2, 100)
backwardPrimes(9900, 10000)
backwardPrimes(501, 509)
