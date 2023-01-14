import matplotlib.pyplot as plt
import pandas as pd
import os
import math
import numpy as np

def delete_char(str,char):
    ls = []
    for i in str:
        if i==char:
            continue
        else:
            ls.append(i)
    return ''.join(ls)
def last_char_index(str,j):
    index = 0
    last_index = 0
    for i in str:
        if i==j:
            last_index = index
        index = index + 1
    return last_index
def cut_char(str,index1,index2):
    index = 0
    ls = []
    for i in str:
        if ( index>=index1 and index<=index2 ):
           ls.append(i)
        index = index + 1
    return ''.join(ls)
def csi_division(str):
    a = 1
    b= 1
    str = delete_char(str,' ')
    if ( '+' in str ):
        index1 = last_char_index(str,'+')
    elif ( '-' in str ):
        index1 = last_char_index(str,'-')
    if 'i' in str:
        index2 = last_char_index(str, 'i')
        real_part = cut_char(str, 0, index1 - 1)
        imaginary_part = cut_char(str, index1 , index2 - 1)
        real_part = float(real_part)
        imaginary_part = float(imaginary_part)
    else:
        real_part = cut_char(str, 0, index1 - 1)
        imaginary_part = 0
    csi = []
    csi.append(real_part)
    csi.append(imaginary_part)
    return csi
def csi_processing( test_point_data ):
    root_max = []
    root_min = []
    change_num = []
    ls = []
    for row in range(451):
        real_part = []
        imaginary_part = []
        for column in range(1, 65):
            csi = csi_division(test_point_data.iloc[row, column])
            real_part.append(csi[0])
            imaginary_part.append(csi[1])
        root = []
        for i in range(64):
            result = math.sqrt(real_part[i] ** 2 + imaginary_part[i] ** 2)
            root.append(result)
        root.sort()
        root_min.append(root[0])
        root_max.append(root[len(root) - 1])
        changeNum = 0
        if imaginary_part[0] >= 0:
            flag = True
        else:
            flag = False
        one = True
        for i in imaginary_part:
            if one == True:
                one = False
            else:
                if flag == True:
                    if i < 0:
                        changeNum = changeNum + 1
                        flag = False
                elif flag == False:
                    if i >= 0:
                        changeNum = changeNum + 1
                        flag = True
        change_num.append(changeNum)
    ls.append( root_max )
    ls.append( root_min )
    ls.append( change_num )
    return ls

coordinate_x = [ x for x in range(451) ]

data_directory = r'C:\Users\Administrator\Desktop\CSI_conplex'

parameter_A = 1/3
parameter_B = 1/3
parameter_C = 1/3

average = []
median = []

for k in range(3,6):
    wknn_x = []
    wknn_y = []
    X = []
    Y = []
    w = 1
    for test_point in os.listdir(data_directory):
        Euclidean_distance = []
        test_point_data = pd.read_excel(data_directory + '\\' + test_point)
        list_test = csi_processing(test_point_data)
        x = test_point_data.iloc[1,65]
        y = test_point_data.iloc[1,66]
        X.append(x)
        Y.append(y)
        for reference_point in os.listdir(data_directory):
            if test_point!=reference_point:
                reference_point_data = pd.read_excel(data_directory+'\\'+reference_point)
                list_reference = csi_processing( reference_point_data )
                max = 0
                min = 0
                change_num = 0
                for i in range(3):
                    for j in range(451):
                        if i==0:
                            max = max + ( list_reference[i][j]-list_test[i][j] )**2
                        elif i==1:
                            min = min + (list_reference[i][j] - list_test[i][j]) ** 2
                        elif i==2:
                            change_num = change_num + (list_reference[i][j] - list_test[i][j]) ** 2
                max = math.sqrt( max )
                min = math.sqrt( min )
                change_num = math.sqrt( change_num )
                euclidean_distance = parameter_A*max + parameter_B*min + parameter_C*change_num
                Euclidean_distance.append(euclidean_distance)
        Euclidean_distance_copy = Euclidean_distance.copy()
        Euclidean_distance.sort()
        list_min = []
        for i in range(0, k):
            list_min.append(Euclidean_distance[i])
        list_index = []
        for i in list_min:
            for j in Euclidean_distance_copy:
                if j == i:
                    index = Euclidean_distance_copy.index(j)
                    list_index.append(index)
                    break
        list_table = os.listdir(data_directory)
        list_table.remove(test_point)
        list_x = []
        list_y = []
        for i in list_index:
            data_name = list_table[i]
            data = pd.read_excel(data_directory + '\\' + data_name)
            x = data.iloc[0, 65]
            y = data.iloc[0, 66]
            list_x.append(x)
            list_y.append(y)
        coordinate = []
        weihted = []
        denominator = 0
        for i in list_min:
            if i == 0:
                i = 1
            denominator = denominator + 1 / i
        for i in range(k):
            if list_min[i] == 0:
                weihted.append(1 / denominator)
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
        wknn_x.append(coordinate[0])
        wknn_y.append(coordinate[1])
        print('---------------------WKNN' + str(w) + '处理完毕---------------------')
        w = w + 1
    # '''画散点图'''
    # x1 = []
    # y1 = []
    # for i in range(0, 29):
    #     x1.append(X[i])
    #     y1.append(Y[i])
    # x2 = []
    # y2 = []
    # for i in range(29, 58):
    #     x2.append(X[i])
    #     y2.append(Y[i])
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
    # plt.savefig(r'C:\Users\Administrator\Desktop\2-2' + '\\' + 'k=' + str(k) + '.png')
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
    # plt.savefig(r'C:\Users\Administrator\Desktop\2-2' + '\\' + 'k= ' + str(k) + '.png')
    # plt.show()
    # '''画散点图'''

    # 画CDF
    x_meter = [a / 1000 for a in X]
    y_meter = [a / 1000 for a in Y]
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
    if k == 3:
        plt.scatter(distance_error, cumulative_probability, s=10, c='red')
    if k == 4:
        plt.scatter(distance_error, cumulative_probability, s=10, c='blue')
    if k == 5:
        plt.scatter(distance_error, cumulative_probability, s=10, c='green')
        # a = list(range(0,18,1))
        # plt.xticks(a)
        plt.legend(['k=3', 'k=4', 'k=5'])
        plt.xlabel('Distance Error(Meter)')
        plt.ylabel('Cumulative Probability')
        plt.show()
    # 画CDF

#     #画条形图
#     x_meter = [a / 1000 for a in X]
#     y_meter = [a / 1000 for a in Y]
#     wknn_x_meter = [a / 1000 for a in wknn_x]
#     wknn_y_meter = [a / 1000 for a in wknn_y]
#     distance_error = []
#     for i in range(0, 58):
#         distance_error_x = (x_meter[i] - wknn_x_meter[i]) ** 2
#         distance_error_y = (y_meter[i] - wknn_y_meter[i]) ** 2
#         distance_error.append(math.sqrt(distance_error_x + distance_error_y))
#     distance_error.sort()
#     cumulative_probability = []
#     for i in distance_error:
#         num = 0
#         for j in distance_error:
#             if j <= i:
#                 num = num + 1
#         cumulative_probability.append(num / 58)
#
#     distance_error_sum = 0
#     for i in distance_error:
#         distance_error_sum = distance_error_sum + i
#     distance_error_average = distance_error_sum / len(distance_error)
#     average.append(distance_error_average)
#     difference = []
#     for i in cumulative_probability:
#         difference.append(abs(i - 0.5))
#     min = difference[0]
#     for i in difference:
#         if i < min:
#             min = i
#     distance_error_median = distance_error[difference.index(min)]
#     median.append(distance_error_median)
# list_x1 = [2.8,3.8,4.8]
# list_x2 = [3,4,5]
# plt.bar(list_x1,average,width=0.2,color='red',label='Average')
# plt.bar(list_x2,median,width=0.2,color='blue',label='Median')
# plt.legend()
# plt.xlabel('K')
# plt.ylabel('Distance Error(Meter)')
# plt.xticks(list(range(3,6)))
# plt.show()
# #画条形图


    #画双轴图
    # ax1 = plt.gca()
    # ax1.plot(coordinate_x,root_min,label = 'min',color = 'red')
    # ax1.plot(coordinate_x,root_max,label = 'max',color = 'blue')
    # plt.xlabel('x')
    # plt.ylabel('root')
    # plt.legend()
    # ax2 = ax1.twinx()
    # ax2.set_ylabel('change_num')
    # ax2.plot(coordinate_x,change_num,label = 'change_num',color = 'black')
    # plt.legend()
    # index1 = last_char_index( table,'e' )
    # index2 = last_char_index( table,'.' )
    # s = cut_char( table,index1+1,index2-1 )
    # plt.savefig(r'C:\Users\Administrator\Desktop\2-2_Figure'+'\\'+'Table'+s+'.png')
    # plt.show()
    #画双轴图











