#Sample Statistic
import math

list_angka = [1, 3, 3, 3, 4, 4, 2, 4]
# list_angka = [1, 4, 3, 4, 3, 1]

def getMean(list):
    sum = 0
    for item in list:
        sum += item
    mean = sum / len(list)
    return mean

def getMedian(list):
    median = 0
    if (len(list)%2 != 0):
        median = list[math.floor(len(list)/2)]
    else:
        mid1 = list[int((len(list)/2)) - 1]
        mid2 = list[int(len(list)/2)]
        median = (mid1 + mid2) / 2
    return median

def getMode(list):
    set_list = set(list)
    mode = []
    dict_list = {}
    for item in list:
        counter = 0
        for item2 in list:
            if item == item2:
                counter += 1
        dict_list[item] = counter
    maxCounter = 0
    for i in dict_list.values():
        if maxCounter < i:
            maxCounter = i  
    for j,k in zip(dict_list.keys(), dict_list.values()):
        if k == maxCounter:
            mode.append(j)
    if len(mode) == len(set_list):
        mode = []
    return mode

def XminMean(list, mean, p):
    XtoMean = 0
    for i in list:
        XtoMean += math.pow((i-mean),p)
    return XtoMean

def getStdev_Sample(n, XtoMean):
    stddev = math.sqrt(getVariance_Sample(n, XtoMean))
    return stddev

def getVariance_Sample(n, XtoMean):
    variance = XtoMean/(n-1)
    return variance

def getVariance_Population(n, XtoMean):
    variance = XtoMean/n
    return variance

def getSkewness(n, variance_population, XtoMean):
    variance = variance_population
    skewness = ((XtoMean/n)/math.pow(variance, 3))
    return skewness

def getExcessKurtosis(n, variance_population, XtoMean):
    variance = variance_population
    kurtosis = ((XtoMean/n)/math.pow(variance, 4)) - 3
    return kurtosis

def statistic_sample(list_angka, menu):
    list_angka.sort()
    n = len(list_angka)
    # mean = getMean(list_angka)
    # median = getMedian(list_angka)
    # mode = getMode(list_angka)
    # XtoMean2 = XminMean(list_angka, mean, 2)
    # XtoMean3 = XminMean(list_angka, mean, 3)
    # XtoMean4 = XminMean(list_angka, mean, 4)
    # stdev = getStdev_Sample(n, XtoMean2)
    # variance = getVariance_Sample(n, XtoMean2)
    # variance_population = getVariance_Population(n, XtoMean2)
    # skewness = getSkewness(n, variance_population, XtoMean3)
    # excess_kurtosis = getExcessKurtosis(n, variance_population, XtoMean4)

    if menu == 'mean':
        mean = getMean(list_angka)
        return mean
    elif menu == 'median':
        median = getMedian(list_angka)
        return median
    elif menu == 'mode':
        mode = getMode(list_angka)
        return mode
    elif menu == 'stdev':
        mean = getMean(list_angka)
        XtoMean2 = XminMean(list_angka, mean, 2)
        stdev = getStdev_Sample(n, XtoMean2)
        return stdev
    elif menu == 'variance':
        mean = getMean(list_angka)
        XtoMean2 = XminMean(list_angka, mean, 2)
        variance = getVariance_Sample(n, XtoMean2)
        return variance
    elif menu == 'skewness':
        mean = getMean(list_angka)
        XtoMean2 = XminMean(list_angka, mean, 2)
        XtoMean3 = XminMean(list_angka, mean, 3)
        variance_population = getVariance_Population(n, XtoMean2)
        skewness = getSkewness(n, variance_population, XtoMean3)
        return skewness
    elif menu == 'excess kurtosis':
        mean = getMean(list_angka)
        XtoMean2 = XminMean(list_angka, mean, 2)
        XtoMean4 = XminMean(list_angka, mean, 4)
        variance_population = getVariance_Population(n, XtoMean2)
        excess_kurtosis = getExcessKurtosis(n, variance_population, XtoMean4)
        return excess_kurtosis

print(statistic_sample(list_angka,'excess kurtosis'))
#pilihan menu:
#mean
#median
#mode
#stdev
#variance
#skewness
#excess kurtosis