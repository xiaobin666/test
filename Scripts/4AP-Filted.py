import matplotlib.pyplot as plt
import pandas as pd
import os
import math
import numpy as np
'''
步骤：
    1、输入文件目录 file_directory
    2、输入保存生成图形的目录 figure_directory
    3、运行程序，即可在目标文件夹自动生成所有定位图
'''
file_directory = r'C:\Users\Administrator\Desktop\Data\HandledData\4AP\Mean(50)+Gauss(30)-Filter'
figure_directory = r'C:\Users\Administrator\Desktop\Localization\4AP\Mean(50)+Gauss(30)-Filter'

def EuclideanDistances(A, B):
    # a = 1
    # b = 1
    # c = 1
    # d = 1
    Euclidean_distance = []
    for i in range(A.shape[1]):
        distance = []
        for j in range(A.shape[0]):
            distance_colume = (A[j, i] - B[j, i]) ** 2
            distance.append(distance_colume)
        sum = 0
        for k in distance:
            sum = sum + k
        Euclidean_distance.append(math.sqrt(sum))
    # sum = 0
    # for i in Euclidean_distance:
    #     sum = sum + i*i
    # result = math.sqrt( sum )
    weishu = 0
    # for i in Euclidean_distance:
    #     if weishu==0:
    #         if i==0:
    #             a = 1
    #         else:
    #             a = 1/i
    #     elif weishu==1:
    #         if i==0:
    #             b = 1
    #         else:
    #             b = 1/i
    #     elif weishu==2:
    #         if i==0:
    #             c = 1
    #         else:
    #             c = 1/i
    #     elif weishu==3:
    #         if i==0:
    #             d = 1
    #         else:
    #             d = 1/i
    #     weishu = weishu + 1
    a = 1
    b = 1
    c = 1
    d = 1
    result = a * Euclidean_distance[0] + b * Euclidean_distance[1] + c * Euclidean_distance[2] + d * Euclidean_distance[3]
    return result
def WKNN(file, m, k):  # file为文件名：xxxx.xlsx , m为CSI矩阵
    list_last = []
    for i in os.listdir(file_directory):
        if i == file:
            continue
        else:
            data = pd.read_excel(file_directory + '\\' + i)
            mat = (data.iloc[:, 1:5]).values
            matrix = np.mat(mat)
            euclidean_distance = EuclideanDistances(m, matrix)
            list_last.append(euclidean_distance)
    list_last_copy = list_last.copy()
    list_last.sort()
    list_min = []
    for i in range(0, k):
        list_min.append(list_last[i])
    list_index = []
    for i in list_min:
        for j in list_last_copy:
            if j == i:
                index = list_last_copy.index(j)
                list_index.append(index)
                break
    list_table = os.listdir(file_directory)
    list_table.remove(file)
    list_x = []
    list_y = []
    for i in list_index:
        data_name = list_table[i]
        data = pd.read_excel(file_directory + '\\' + data_name)
        x = data.iloc[0, 5]
        y = data.iloc[0, 6]
        list_x.append(x)
        list_y.append(y)
    coordinate = []
    '''加权'''
    # if 0 in list_min:
    #
    #
    #
    #     index = list_min.index(0)
    #     index1 = list_x[index]
    #     index2 = list_y[index]
    #     coordinate.append(index1)
    #     coordinate.append(index2)
    # else:
    weihted = []
    denominator = 0

    for i in list_min:
        if i != 0:
            quanzhi = i
            break

    for i in list_min:
        if i == 0:
            i = quanzhi / 2
        denominator = denominator + 1 / i
    for i in range(k):
        if list_min[i] == 0:
            weihted.append((quanzhi / 2) / denominator)
        else:
            weihted.append((1 / list_min[i]) / denominator)
    weihted_x = 0
    index_x = 0
    for i in list_x:
        weihted_x = weihted_x + weihted[index_x] * i
        index_x = index_x + 1
    weihted_y = 0
    index_y = 0
    for i in list_y:
        weihted_y = weihted_y + weihted[index_y] * i
        index_y = index_y + 1
    # for i in range(k):
    #     if i==0:
    #         weihted.append(3/5)
    #     if i==1:
    #         weihted.append(2/5)
    #     if i==2:
    #         weihted.append(1/4)
    #     if i==3:
    #         weihted.append(1/4)
    weihted_x = 0
    index_x = 0
    for i in list_x:
        weihted_x = weihted_x + weihted[index_x] * i
        index_x = index_x + 1
    weihted_y = 0
    index_y = 0
    for i in list_y:
        weihted_y = weihted_y + weihted[index_y] * i
        index_y = index_y + 1
    coordinate.append(weihted_x)
    coordinate.append(weihted_y)
    '''加权'''
    return coordinate

average = []
median = []
figure1 = plt.figure()
ax1 = figure1.add_subplot(111)
figure2 = plt.figure()
ax2 = figure2.add_subplot(111)
figure3 = plt.figure()
ax3 = figure3.add_subplot(111)
for k in range(3, 4):
    wknn_x = []
    wknn_y = []
    x = []
    y = []
    index = 1
    for test_point in os.listdir(file_directory):
        data = pd.read_excel(file_directory + '\\' + test_point)
        x.append(data.iloc[1, 5])
        y.append(data.iloc[1, 6])
        rss = data.iloc[:, 1:5].values
        rss_matrix = np.matrix(rss)
        wknn_coordinate = WKNN(test_point, rss_matrix, k)
        wknn_x.append(wknn_coordinate[0])
        wknn_y.append(wknn_coordinate[1])
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
    for i in range(29, 59):
        x2.append(x[i])
        y2.append(y[i])
    wknn_x1 = []
    wknn_y1 = []
    for i in range(0, 29):
        wknn_x1.append(wknn_x[i])
        wknn_y1.append(wknn_y[i])
    wknn_x2 = []
    wknn_y2 = []
    for i in range(29, 59):
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
    for i, txt in enumerate(np.arange(29, 59)):
        plt.annotate(txt, (x2[i], y2[i]))
        plt.annotate(txt, (wknn_x2[i], wknn_y2[i]))
    plt.legend(['ActualCoordinate', 'W   knnedCoordinate'])
    plt.xlabel('x', size=14)
    plt.ylabel("y", size=14)
    plt.title('K = ' + str(k))
    plt.savefig(figure_directory + '\\' + 'k= ' + str(k) + '.png')
    # plt.show()
    '''画散点图'''
    # # 画CDF
    x_meter = [a / 1000 for a in x]
    y_meter = [a / 1000 for a in y]
    wknn_x_meter = [a / 1000 for a in wknn_x]
    wknn_y_meter = [a / 1000 for a in wknn_y]
    distance_error = []
    for i in range(0, 59):
        distance_error_x = (x_meter[i] - wknn_x_meter[i]) ** 2
        distance_error_y = (y_meter[i] - wknn_y_meter[i]) ** 2
        distance_error.append(math.sqrt(distance_error_x + distance_error_y))
    distance_error_copy = distance_error.copy()
    distance_error.sort()
    cumulative_probability = []
    for i in distance_error:
        num = 0
        for j in distance_error:
            if j <= i:
                num = num + 1
        cumulative_probability.append(num / 58)
    if k == 3:
        ax1.scatter(distance_error, cumulative_probability, s=10, c='red')
        ax1.legend(['k=3', 'k=4', 'k=5'])
        ax1.set_xlabel('Distance Error(Meter)')
        ax1.set_ylabel('Cumulative Probability')
        figure1.savefig(figure_directory + '\\' + 'Figure_1.png')
    # 画CDF
    # 画点误差图
    list_spot_num = [i for i in range(len(distance_error_copy))]
    if k == 3:
        ax2.plot(list_spot_num, distance_error_copy, c='blue')
        ax2.legend(['k=3', 'k=4', 'k=5'])
        ax2.set_xlabel('Spot number')
        ax2.set_ylabel('Positioning Error')
        figure2.savefig(figure_directory + '\\' + 'spot_distance_error.png')
    dataframe = pd.DataFrame()
    dataframe.insert(0, 'Error-K=3', distance_error_copy)
    coordinate = []
    for i in range(len(x)):
        zuobiao = (x[i], y[i])
        coordinate.append(zuobiao)
    dataframe.insert(1, 'Coordinate', coordinate)

    Wnn_coordinate = []
    for i in range(len(wknn_x)):
        zuobiao = (wknn_x[i], wknn_y[i])
        Wnn_coordinate.append(zuobiao)
    dataframe.insert(2, 'Wknned-Coordinate', Wnn_coordinate)

    writer = pd.ExcelWriter(r'C:\Users\Administrator\Desktop\Localization\4AP\Mean(50)+Gauss(30)-Filter' + '\\' + 'Distance-Error.xlsx')
    dataframe.to_excel(writer, index=False)
    writer.save()

    # 画点误差图
    # 画条形图
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
list_x1 = [2.8, 3.8, 4.8]
list_x2 = [3, 4, 5]
ax3.bar(list_x1, average, width=0.2, color='red', label='Average')
ax3.bar(list_x2, median, width=0.2, color='blue', label='Median')
ax3.legend()
ax3.set_xlabel('K')
ax3.set_ylabel('Distance Error(Meter)')
ax3.set_xticks(list(range(3, 6)))
figure3.savefig(figure_directory + '\\' + 'Figure_2.png')
# ax3.show()
# 画条形图


