
import matplotlib.pyplot as plt
import pandas as pd
import os
import math
import numpy as np
data_directory = r'C:\Users\Administrator\Desktop\4AP-thrid'
def EuclideanDistances(A, B):
    # a = 1
    # b = 1
    # c = 1
    # d = 1
    Euclidean_distance = []
    for i in range( A.shape[1] ):
        distance = []
        for j in range( A.shape[0] ):
            distance_colume = ( A[j,i]-B[j,i] )**2
            distance.append(distance_colume)
        sum = 0
        for k in distance:
            sum = sum + k
        Euclidean_distance.append( math.sqrt(sum) )
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
    # result = a*Euclidean_distance[0] + b*Euclidean_distance[1] + c*Euclidean_distance[2] + d*Euclidean_distance[3]
    result = a*Euclidean_distance[0]*Euclidean_distance[0] + b*Euclidean_distance[1]*Euclidean_distance[1] + c*Euclidean_distance[2]*Euclidean_distance[2] + d*Euclidean_distance[3]*Euclidean_distance[3]
    result = math.sqrt(result)
    return result
def WKNN( file , m , k ):   #file为文件名：xxxx.xlsx , m为CSI矩阵
    list_last = []
    for i in os.listdir(data_directory):
        if i==file:
            # continue
            data = pd.read_excel(data_directory + '\\' + i)
            mat = (data.iloc[:, 0:4]).values
            matrix = np.mat(mat)
            euclidean_distance = EuclideanDistances(m, matrix)
            list_last.append(euclidean_distance)
        else:
            data = pd.read_excel(data_directory + '\\' + i)
            mat = ( data.iloc[:,0:4] ).values
            matrix = np.mat(mat)
            euclidean_distance = EuclideanDistances(m,matrix)
            list_last.append(euclidean_distance)
    list_last_copy = list_last.copy()
    list_last.sort()
    list_min = []
    for i in range(0,k):
        list_min.append(list_last[i])
    list_index = []
    for i in list_min:
        for j in list_last_copy:
            if j==i:
                index = list_last_copy.index(j)
                list_index.append(index)
                break
    list_table = os.listdir(data_directory)
    # list_table.remove(file)
    list_x = []
    list_y = []
    for i in list_index:
        data_name = list_table[i]
        data = pd.read_excel(data_directory + '\\' + data_name)
        x = data.iloc[0,4]
        y = data.iloc[0,5]
        list_x.append(x)
        list_y.append(y)
    coordinate = []
    # '''未加权'''
    # sum_x = 0
    # sum_y = 0
    # for i in list_x:
    #     sum_x = sum_x + i
    # for i in list_y:
    #     sum_y = sum_y + i
    # coordinate_x = sum_x/len(list_x)
    # coordinate_y = sum_y/len(list_y)
    # coordinate.append(coordinate_x)
    # coordinate.append(coordinate_y)
    # '''未加权'''

    '''加权'''
    weihted = []
    denominator = 0
    for i in list_min:
        if i==0:
            i=1
            print('出现')
        denominator = denominator + 1 / i
    for i in range(k):
        if list_min[i]==0:
            weihted.append( 1/denominator )
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
    coordinate.append(weihted_x)
    coordinate.append(weihted_y)
    '''加权'''
    return coordinate
average = []
median = []
for k in range(3,6):
    a = 0
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
        x.append( data.iloc[1,4] )
        y.append( data.iloc[1,5] )
        rss = data.iloc[:,0:4].values
        rss_matrix = np.matrix(rss)
        wknn_coordinate = WKNN(test_point, rss_matrix ,k)
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
    # for i in range(29, 59):
    #     x2.append(x[i])
    #     y2.append(y[i])
    # wknn_x1 = []
    # wknn_y1 = []
    # for i in range(0, 29):
    #     wknn_x1.append(wknn_x[i])
    #     wknn_y1.append(wknn_y[i])
    # wknn_x2 = []
    # wknn_y2 = []
    # for i in range(29, 59):
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
    # plt.savefig(r'C:\Users\Administrator\Desktop\4AP_RSS_3' + '\\' + 'k=' + str(k) + '.png')
    # plt.show()
    # plt.scatter(x2, y2, s=1, c='red', label='a')
    # plt.scatter(wknn_x2, wknn_y2, s=1, c='blue', label='b')
    # for i, txt in enumerate(np.arange(29, 59)):
    #     plt.annotate(txt, (x2[i], y2[i]))
    #     plt.annotate(txt, (wknn_x2[i], wknn_y2[i]))
    # plt.legend(['ActualCoordinate', 'WknnedCoordinate'])
    # plt.xlabel('x', size=14)
    # plt.ylabel("y", size=14)
    # plt.title('K = ' + str(k))
    # plt.savefig(r'C:\Users\Administrator\Desktop\4AP_RSS_3' + '\\' + 'k= ' + str(k) + '.png')
    # plt.show()
    # '''画散点图'''
    # 画CDF
    x_meter = [a / 1000 for a in x]
    y_meter = [a / 1000 for a in y]
    wknn_x_meter = [a / 1000 for a in wknn_x]
    wknn_y_meter = [a / 1000 for a in wknn_y]
    distance_error = []
    for i in range(0, 59):
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
