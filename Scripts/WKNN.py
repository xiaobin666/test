import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import math

'''
步骤：
    1、输入文件目录 file_directory
    2、输入保存生成图形的目录 figure_directory
    3、运行程序，即可在目标文件夹自动生成所有定位图
'''
file_directory = r'C:\Users\Administrator\Desktop\RSS-data\SingleAP\HandleData'
figure_directory = r'C:\Users\Administrator\Desktop\Rss-Localization\SingleAp\1-2-1'

def WKNN( file , ls ,k ):   #file为文件名：xxxx.xlsx
    list_last = []
    for i in os.listdir(file_directory):
        if i==file:
            # continue
            data = pd.read_excel(file_directory + '\\' + i)
            list_test = data.iloc[:, 1].tolist()
            euclidean_distance = 0
            for j in range(0, 451):
                euclidean_distance = euclidean_distance + (ls[j] - list_test[j]) ** 2
            euclidean_distance = math.sqrt(euclidean_distance)
            list_last.append(euclidean_distance)
        else:
            data = pd.read_excel(file_directory + '\\' + i)
            list_test = data.iloc[:, 1].tolist()
            euclidean_distance = 0
            for j in range(0, 451):
                euclidean_distance = euclidean_distance + (ls[j] - list_test[j]) **2
            euclidean_distance = math.sqrt(euclidean_distance)
            list_last.append(euclidean_distance)
    list_last_copy = []
    for i in list_last:
        list_last_copy.append(i)
    list_last.sort()
    list_min = []
    for i in range(0,k):
        list_min.append(list_last[i])
    weighted = []
    denominator = 0
    # print(list_min)
    for i in list_min:
        if i==0:
            index_0 = list_min.index(i)
            i = (1/2)*list_min[ index_0+1 ]
            # print(list_min[ index_0+1 ])
        denominator = denominator + 1/i
    for i in range(k):
        if list_min[i]==0:
            index_0 = list_min.index(0)
            w = (1/2)*list_min[ index_0+1 ]
            weighted.append( (1/w)/denominator)
        else:
            weighted.append( ( 1/list_min[i] )/denominator )

    list_index = []
    for i in list_min:
        for j in list_last_copy:
            if j==i:
                index = list_last_copy.index(j)
                list_index.append(index)
                break
    list_table = os.listdir(file_directory)
    # list_table.remove(file)
    list_x = []
    list_y = []
    for i in list_index:
        data_name = list_table[i]
        data = pd.read_excel(file_directory + '\\' + data_name)
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
    # '''均值'''
    # sum_x = 0
    # for i in list_x:
    #     sum_x = sum_x + i
    # sum_y = 0
    # for i in list_y:
    #     sum_y = sum_y + i
    # coordinate.append( sum_x/len(list_x) )
    # coordinate.append( sum_y/len(list_y) )
    # '''均值'''
    return coordinate
average = []
median = []
figure1 = plt.figure()
ax1 = figure1.add_subplot(111)
figure2 = plt.figure()
ax2 = figure2.add_subplot(111)
figure3 = plt.figure()
ax3 = figure3.add_subplot(111)
for k in range(3,6):
    wknn_x = []
    wknn_y = []
    x = []
    y = []
    index = 1
    for i in os.listdir(file_directory):
        data = pd.read_excel(file_directory + '\\' + i)
        x.append(data.iloc[0, 3])
        y.append(data.iloc[0, 4])
        wknn_list = WKNN(i, data.iloc[:, 2].tolist(), k)
        wknn_x.append(wknn_list[0])
        wknn_y.append(wknn_list[1])
        print('---------------------WKNN' + str(index) + '处理完毕---------------------')
        index = index + 1
    '''画散点图'''
    x1 = []
    y1 = []
    for i in range(0, 29):
        x1.append(x[i])
        y1.append(y[i])
    x2 = []
    y2 = []
    for i in range(29, 58):
        x2.append(x[i])
        y2.append(y[i])
    wknn_x1 = []
    wknn_y1 = []
    for i in range(0, 29):
        wknn_x1.append(wknn_x[i])
        wknn_y1.append(wknn_y[i])
    wknn_x2 = []
    wknn_y2 = []
    for i in range(29, 58):
        wknn_x2.append(wknn_x[i])
        wknn_y2.append(wknn_y[i])
    plt.figure()
    plt.scatter(x1, y1, s=1, c='red', label='a')
    plt.scatter(wknn_x1, wknn_y1, s=1, c='blue', label='b')
    for i, txt in enumerate(np.arange(29)):
        plt.annotate(txt, (x1[i], y1[i]))
        plt.annotate(txt, (wknn_x1[i], wknn_y1[i]))
    plt.legend(['ActualCoordinate', 'WknnedCoordinate'])
    plt.xlabel('x', size=14)
    plt.ylabel("y", size=14)
    plt.title('K = ' + str(k))
    plt.savefig(figure_directory + '\\' + 'k=' + str(k) + '.png')
    # plt.show()
    plt.figure()
    plt.scatter(x2, y2, s=1, c='red', label='a')
    plt.scatter(wknn_x2, wknn_y2, s=1, c='blue', label='b')
    for i, txt in enumerate(np.arange(29, 58)):
        plt.annotate(txt, (x2[i], y2[i]))
        plt.annotate(txt, (wknn_x2[i], wknn_y2[i]))
    plt.legend(['ActualCoordinate', 'WknnedCoordinate'])
    plt.xlabel('x', size=14)
    plt.ylabel("y", size=14)
    plt.title('K = ' + str(k))
    plt.savefig(figure_directory + '\\' + 'k= ' + str(k) + '.png')
    # plt.show()

    #画CDF
    x_meter = [ a/1000 for a in x ]
    y_meter = [ a/1000 for a in y ]
    wknn_x_meter = [ a/1000 for a in wknn_x ]
    wknn_y_meter = [ a/1000 for a in wknn_y ]
    distance_error = []
    for i in  range(0,58):
        distance_error_x = ( x_meter[i] - wknn_x_meter[i] )**2
        distance_error_y = ( y_meter[i] - wknn_y_meter[i] )**2
        distance_error.append( math.sqrt( distance_error_x + distance_error_y   ) )
    distance_error_copy = distance_error.copy()
    distance_error.sort()
    cumulative_probability = []
    for i in distance_error:
        num = 0
        for j in distance_error:
            if j<=i:
                num = num + 1
        cumulative_probability.append(num/58)
    if k==3:
        ax1.scatter(distance_error,cumulative_probability,s=10,c='red')
        # plt.plot(distance_error,cumulative_probability,c='red')
    if k==4:
        ax1.scatter(distance_error,cumulative_probability,s=10,c='blue')
        # plt.plot(distance_error,cumulative_probability,c='blue')
    if k==5:
        ax1.scatter(distance_error,cumulative_probability,s=10,c='green')
        # plt.plot(distance_error,cumulative_probability,c='green')
        # a = list(range(0,18,1))
        # plt.xticks(a)
        ax1.legend(['k=3','k=4','k=5'])
        ax1.set_xlabel('Distance Error(Meter)')
        ax1.set_ylabel('Cumulative Probability')
        figure1.savefig(figure_directory + '\\' + 'Figure_1.png')

    # 画点误差图
    list_spot_num = [i for i in range(len(distance_error_copy))]
    if k == 3:
        ax2.plot(list_spot_num, distance_error_copy, c='red')
    if k == 4:
        ax2.plot(list_spot_num, distance_error_copy, c='blue')
    if k == 5:
        ax2.plot(list_spot_num, distance_error_copy, c='green')
        # a = list(range(0,18,1))
        # plt.xticks(a)
        ax2.legend(['k=3', 'k=4', 'k=5'])
        ax2.set_xlabel('Spot number')
        ax2.set_ylabel('Positioning Error')
        figure2.savefig(figure_directory + '\\' + 'spot_distance_error.png')
    # 画点误差图

    distance_error_sum = 0
    for i in distance_error:
        distance_error_sum = distance_error_sum + i
    distance_error_average = distance_error_sum/len(distance_error)
    average.append(distance_error_average)
    difference = []
    for i in cumulative_probability:
        difference.append(abs(i-0.5))
    min = difference[0]
    for i in difference:
        if i<min:
            min = i
    distance_error_median = distance_error[difference.index(min)]
    median.append(distance_error_median)

list_x1 = [2.8,3.8,4.8]
list_x2 = [3,4,5]
ax3.bar(list_x1,average,width=0.2,color='red',label='Average')
ax3.bar(list_x2,median,width=0.2,color='blue',label='Median')
ax3.legend()
ax3.set_xlabel('K')
ax3.set_ylabel('Distance Error(Meter)')
ax3.set_xticks(list(range(3,6)))
figure3.savefig(figure_directory + '\\' + 'Figure_2.png')
