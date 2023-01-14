import math
import os
import xlrd
import numpy as np
import matplotlib.pyplot as plt
import keyboard
import pandas as pd
A = 1
B = 5
u = 0
H = 1
# x_last = -65
p_last = 10
data_directory = r'C:\Users\Administrator\Desktop\RSS'
def get_data_test(data_name):
    list_result = []
    data = xlrd.open_workbook(data_name)
    dataSheet = data.sheets()[0]
    list_actual = []
    list_predict = []
    firstValue = 0
    flag = 0
    for i in dataSheet.col_values(2):
        if flag == 1:
            firstValue = i
            break
        flag = flag + 1
    x_last = firstValue
    j = 0
    for i in dataSheet.col_values(2):
        if (j > 0):
            f = int(i)
            list_actual.append(f)
            x_predict, p_last, x_last = kalman(f, x_last, 10)
            list_predict.append(x_predict)
        j = j + 1
    x = np.linspace(0, len(list_actual), len(list_actual))
    y_actual = list_actual
    y_predict = list_predict
    rounded_list = []
    for i in list_predict:
        rounded_list.append(round(i, 10))
    list_predict_copy = list_predict.copy()
    list_predict_copy.sort()
    MIN = list_predict_copy[0]
    MAX = list_predict_copy[len(list_predict_copy) - 1]
    MAX_reduce_MIN = MAX - MIN
    two = False
    index = 0
    peak_number = 0
    # valley_number = 0
    list_peak = []
    for i in rounded_list:
        if two == False:
            two = True
            index = index + 1
        else:
            if index != (len(rounded_list) - 1):
                if ( (rounded_list[index] >= rounded_list[index - 1]) and (rounded_list[index] > rounded_list[index + 1]) ):
                    if ((rounded_list[index] - rounded_list[index - 1])) >= 0 and (
                            (rounded_list[index] - rounded_list[index + 1]) > 0.05):
                        peak_number = peak_number + 1
                        list_peak.append(index)
                        # print('index:' + str(index))
                elif (rounded_list[index] > rounded_list[index - 1] and rounded_list[index] >= rounded_list[index + 1]):
                    if ((rounded_list[index] - rounded_list[index - 1]) > 0) and (
                            (rounded_list[index] - rounded_list[index + 1]) >= 0.05):
                        peak_number = peak_number + 1
                        list_peak.append(index)
                        # print('index:' + str(index))
                # if (rounded_list[index] <= rounded_list[index - 1] and rounded_list[index] < rounded_list[index + 1]) or (rounded_list[index] < rounded_list[index - 1] and rounded_list[index] <= rounded_list[index + 1]):
                #     valley_number = valley_number + 1
            index = index + 1
    # print('peak_number:' + str(peak_number))

    # qi = []
    # for q in  list_peak:
    #     qi.append( rounded_list[q] )

    # print(list_peak)
    # print(rounded_list)
    # print(qi)

    difference = []
    for j in range(len(list_peak) - 1):
        differ = list_peak[j + 1] - list_peak[j]
        difference.append(differ)
    sum_peak = 0
    for i in difference:
        sum_peak = sum_peak + i
    if len(difference) == 0:
        average_peak = 0
    else:
        average_peak = sum_peak / len(difference)

    # print('difference: ', difference)
    # print('average_peak', average_peak)
    list_result.append(MAX)
    list_result.append(MIN)
    list_result.append(MAX_reduce_MIN)
    list_result.append(peak_number)
    list_result.append(average_peak)

    # print('MAX: ', MAX)
    # print('MIN: ', MIN)
    # print('MAX_reduce_MIN: ', MAX_reduce_MIN)
    # print('peak_number: ', peak_number)
    # print('difference: ', difference)
    # print('average_peak: ', average_peak)

    # plt.plot(x,y_actual)
    # plt.plot(x,y_predict)
    # plt.legend(['y_actual','y_predict'])
    # plt.show()

    return list_result
def kalman(z_measure,x_last,p_last, Q=0.1, R=20):
    x_mid = A*x_last + B*u
    p_mid = A*p_last*A + Q
    kg = p_mid*H/( H*p_mid*H + R)
    x_now = x_mid + kg*(z_measure - H*x_mid)
    p_now = (1-kg*H)*p_mid
    p_last = p_now
    x_last = x_now
    return x_now,p_last,x_last
def get_data(data_name):
    list_result = []
    data = xlrd.open_workbook(data_name)
    dataSheet = data.sheets()[0]
    list_actual = []
    list_predict = []
    firstValue = 0
    flag = 0
    for i in dataSheet.col_values(1):
        if flag == 1:
            firstValue = i
            break
        flag = flag + 1
    x_last = firstValue
    j = 0
    for i in dataSheet.col_values(1):
        if (j > 0):
            f = int(i)
            list_actual.append(f)
            x_predict, p_last, x_last = kalman(f, x_last, 10)
            list_predict.append(x_predict)
        j = j + 1

    x = np.linspace(0, len(list_actual), len(list_actual))
    y_actual = list_actual
    y_predict = list_predict

    rounded_list = []
    for i in list_predict:
        rounded_list.append(round(i, 10))
    list_predict_copy = list_predict.copy()
    list_predict_copy.sort()
    MIN = list_predict_copy[0]
    MAX = list_predict_copy[len(list_predict_copy) - 1]
    MAX_reduce_MIN = MAX - MIN
    two = False
    index = 0
    peak_number = 0
    # valley_number = 0
    list_peak = []
    for i in rounded_list:
        if two == False:
            two = True
            index = index + 1
        else:
            if index != (len(rounded_list) - 1):
                if ( (rounded_list[index] >= rounded_list[index - 1]) and (rounded_list[index] > rounded_list[index + 1]) ):
                    if ((rounded_list[index] - rounded_list[index - 1])) >= 0 and (
                            (rounded_list[index] - rounded_list[index + 1]) > 0.05):
                        peak_number = peak_number + 1
                        list_peak.append(index)
                        # print('index:' + str(index))
                elif (rounded_list[index] > rounded_list[index - 1] and rounded_list[index] >= rounded_list[index + 1]):
                    if ((rounded_list[index] - rounded_list[index - 1]) > 0) and (
                            (rounded_list[index] - rounded_list[index + 1]) >= 0.05):
                        peak_number = peak_number + 1
                        list_peak.append(index)
                        # print('index:' + str(index))
                # if (rounded_list[index] <= rounded_list[index - 1] and rounded_list[index] < rounded_list[index + 1]) or (rounded_list[index] < rounded_list[index - 1] and rounded_list[index] <= rounded_list[index + 1]):
                #     valley_number = valley_number + 1
            index = index + 1
    # print('peak_number:' + str(peak_number))

    # qi = []
    # for q in  list_peak:
    #     qi.append( rounded_list[q] )

    # print(list_peak)
    # print(rounded_list)
    # print(qi)

    difference = []
    for j in range(len(list_peak) - 1):
        differ = list_peak[j + 1] - list_peak[j]
        difference.append(differ)
    sum_peak = 0
    for i in difference:
        sum_peak = sum_peak + i
    if len(difference) == 0:
        average_peak = 0
    else:
        average_peak = sum_peak / len(difference)

    # print('difference: ', difference)
    # print('average_peak', average_peak)
    list_result.append(MAX)
    list_result.append(MIN)
    list_result.append(MAX_reduce_MIN)
    list_result.append(peak_number)
    list_result.append(average_peak)

    # print('MAX: ', MAX)
    # print('MIN: ', MIN)
    # print('MAX_reduce_MIN: ', MAX_reduce_MIN)
    # print('peak_number: ', peak_number)
    # print('difference: ', difference)
    # print('average_peak: ', average_peak)

    # plt.plot(x,y_actual)
    # plt.plot(x,y_predict)
    # plt.legend(['y_actual','y_predict'])
    # plt.show()

    return list_result
def WKNN( test_point ,k):   #file为文件名：xxxx.xlsx
    list_last = []
    list_data_test = get_data_test( r'C:\Users\Administrator\Desktop\RSS' + '\\' + test_point )
    for reference_point in os.listdir(r'C:\Users\Administrator\Desktop\RSS'):
        if reference_point != test_point:
            list_data_reference = get_data( r'C:\Users\Administrator\Desktop\RSS' + '\\' + reference_point)
            distance = euclideanDistances(list_data_test,list_data_reference)
            list_last.append(distance)
        else:
            list_data_reference = get_data(r'C:\Users\Administrator\Desktop\RSS' + '\\' + reference_point)
            distance = euclideanDistances(list_data_test, list_data_reference)
            list_last.append(distance)

    list_last_copy = []
    for i in list_last:
        list_last_copy.append(i)
    list_last.sort()
    list_min = []
    for i in range(0,k):
        list_min.append(list_last[i])
    weighted = []
    denominator = 0
    for i in list_min:
        if i==0:
            print('出现0')
            i = 1
        denominator = denominator + 1/i
    for i in range(k):
        if list_min[i]==0:
            weighted.append(1/denominator)
        else:
            weighted.append( ( 1/list_min[i] )/denominator )
    list_index = []
    for i in list_min:
        for j in list_last_copy:
            if j==i:
                index = list_last_copy.index(j)
                list_index.append(index)
                break
    list_table = os.listdir(data_directory)
    # list_table.remove(test_point)
    list_x = []
    list_y = []
    for i in list_index:
        data_name = list_table[i]
        data = pd.read_excel(data_directory + '\\' + data_name)
        x = data.iloc[0,3]
        y = data.iloc[0,4]
        list_x.append(x)
        list_y.append(y)
    coordinate = []

    weighted_x = 0
    index_x = 0
    for i in list_x:
        weighted_x = weighted_x + weighted[index_x]*i
        index_x = index_x + 1

    index_y = 0
    weighted_y = 0
    for i in list_y:
        weighted_y = weighted_y + weighted[index_y]*i
        index_y = index_y + 1

    coordinate.append(weighted_x)
    coordinate.append(weighted_y)
    return coordinate
def euclideanDistances(list_data_test,list_data_reference):
    a = 1
    b = 1
    c = 1
    d = 1000
    e = 10
    sum = 0
    for i in range(5):
        if i == 0:
            di = a * (list_data_test[i] - list_data_reference[i]) * (list_data_test[i] - list_data_reference[i])
            sum = sum + di
        elif i == 1:
            di = b * (list_data_test[i] - list_data_reference[i]) * (list_data_test[i] - list_data_reference[i])
            sum = sum + di
        elif i == 2:
            di = c * (list_data_test[i] - list_data_reference[i]) * (list_data_test[i] - list_data_reference[i])
            sum = sum + di
        elif i == 3:
            di = d * (list_data_test[i] - list_data_reference[i]) * (list_data_test[i] - list_data_reference[i])
            sum = sum + di
        elif i == 4:
            di = e * (list_data_test[i] - list_data_reference[i]) * (list_data_test[i] - list_data_reference[i])
            sum = sum + di
    euclideanDistances = math.sqrt(sum)

    # if euclideanDistances==0:
    #     print(list_data_test)
    #     print(list_data_reference)
    #     print(di)

    return euclideanDistances
average = []
median = []
for k in range(3,6):
    wknn_x = []
    wknn_y = []
    x = []
    y = []
    index = 1
    for test_point in os.listdir(data_directory):
        # data = pd.read_excel(data_directory + '\\' + i)
        # x.append(data.iloc[0, 2])
        # y.append(data.iloc[0, 3])
        # wknn_list = WKNN(i, data.iloc[:, 1].tolist(), k)
        # wknn_x.append(wknn_list[0])
        # wknn_y.append(wknn_list[1])
        data = pd.read_excel(data_directory + '\\' + test_point)
        x.append( data.iloc[1,3] )
        y.append( data.iloc[1,4] )
        wknn_coordinate = WKNN(test_point, k)
        wknn_x.append( wknn_coordinate[0] )
        wknn_y.append( wknn_coordinate[1] )
        print('---------------------WKNN' + str(index) + '处理完毕---------------------')
        index = index + 1

    # '''画散点图'''
    # x1 = []
    # y1 = []
    # for i in range(0, 29):
    #     x1.append(x[i])
    #     y1.append(y[i])
    # x2 = []
    # y2 = []
    # for i in range(29, 58):
    #     x2.append(x[i])
    #     y2.append(y[i])
    # wknn_x1 = []
    # wknn_y1 = []
    # for i in range(0, 29):
    #     wknn_x1.append(wknn_x[i])
    #     wknn_y1.append(wknn_y[i])
    # wknn_x2 = []
    # wknn_y2 = []
    # for i in range(29, 58):
    #     wknn_x2.append(wknn_x[i])
    #     wknn_y2.append(wknn_y[i])
    # plt.scatter(x1, y1, s=1, c='red', label='a')
    # plt.scatter(wknn_x1, wknn_y1, s=1, c='blue', label='b')
    # for i, txt in enumerate(np.arange(29)):
    #     plt.annotate(txt, (x1[i], y1[i]))
    #     plt.annotate(txt, (wknn_x1[i], wknn_y1[i]))
    # plt.legend(['ActualCoordinate', 'WknnedCoordinate'])
    # plt.xlabel('x', size=14)
    # plt.ylabel("y", size=14)
    # plt.title('K = ' + str(k))
    # plt.savefig(r'C:\Users\Administrator\Desktop\1-2-2' + '\\' + 'k=' + str(k) + '.png')
    # plt.show()
    # plt.scatter(x2, y2, s=1, c='red', label='a')
    # plt.scatter(wknn_x2, wknn_y2, s=1, c='blue', label='b')
    # for i, txt in enumerate(np.arange(29, 58)):
    #     plt.annotate(txt, (x2[i], y2[i]))
    #     plt.annotate(txt, (wknn_x2[i], wknn_y2[i]))
    # plt.legend(['ActualCoordinate', 'WknnedCoordinate'])
    # plt.xlabel('x', size=14)
    # plt.ylabel("y", size=14)
    # plt.title('K = ' + str(k))
    # plt.savefig(r'C:\Users\Administrator\Desktop\1-2-2' + '\\' + 'k= ' + str(k) + '.png')
    # plt.show()
    # '''画散点图'''


    # 画CDF
    x_meter = [a / 1000 for a in x]
    y_meter = [a / 1000 for a in y]
    wknn_x_meter = [a / 1000 for a in wknn_x]
    wknn_y_meter = [a / 1000 for a in wknn_y]
    distance_error = []
    for i in range(0, 58):
        distance_error_x = (x_meter[i] - wknn_x_meter[i]) ** 2
        distance_error_y = (y_meter[i] - wknn_y_meter[i]) ** 2
        distance_error.append(math.sqrt(distance_error_x + distance_error_y))
    distance_error.sort()
    cumulative_probability = []
    for i in distance_error:
        num = 0
        for j in distance_error:
            if j <= i:
                num = num + 1
        cumulative_probability.append(num / 58)
    if k==3:
        plt.scatter(distance_error,cumulative_probability,s=10,c='red')
    if k==4:
        plt.scatter(distance_error,cumulative_probability,s=10,c='blue')
    if k==5:
        plt.scatter(distance_error,cumulative_probability,s=10,c='green')
        # a = list(range(0,18,1))
        # plt.xticks(a)
        plt.legend(['k=3','k=4','k=5'])
        plt.xlabel('Distance Error(Meter)')
        plt.ylabel('Cumulative Probability')
        plt.show()
    # 画CDF



    #画条形图
    x_meter = [a / 1000 for a in x]
    y_meter = [a / 1000 for a in y]
    wknn_x_meter = [a / 1000 for a in wknn_x]
    wknn_y_meter = [a / 1000 for a in wknn_y]
    distance_error = []
    for i in range(0, 58):
        distance_error_x = (x_meter[i] - wknn_x_meter[i]) ** 2
        distance_error_y = (y_meter[i] - wknn_y_meter[i]) ** 2
        distance_error.append(math.sqrt(distance_error_x + distance_error_y))
    distance_error.sort()
    cumulative_probability = []
    for i in distance_error:
        num = 0
        for j in distance_error:
            if j <= i:
                num = num + 1
        cumulative_probability.append(num / 58)

    distance_error_sum = 0
    for i in distance_error:
        distance_error_sum = distance_error_sum + i
    distance_error_average = distance_error_sum / len(distance_error)
    average.append(distance_error_average)

    difference = []
    for i in cumulative_probability:
        difference.append(abs(i - 0.5))
    min = difference[0]
    for i in difference:
        if i < min:
            min = i
    distance_error_median = distance_error[difference.index(min)]
    median.append(distance_error_median)
list_x1 = [2.8,3.8,4.8]
list_x2 = [3,4,5]
plt.bar(list_x1,average,width=0.2,color='red',label='Average')
plt.bar(list_x2,median,width=0.2,color='blue',label='Median')
plt.legend()
plt.xlabel('K')
plt.ylabel('Distance Error(Meter)')
plt.xticks(list(range(3,6)))
plt.show()
#画条形图