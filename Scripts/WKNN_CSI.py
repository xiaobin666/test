import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

data_directory = r'C:\Users\Administrator\Desktop\CSI'
def EuclideanDistances(A, B):
    BT = B.transpose()
    ABT = np.dot(A,BT)
    ls_A = []
    for i in range(0,A.shape[0]):
        result = 0
        ls_son_A = []
        for j in range(0,A.shape[1]):
            result = result + A[i,j]*A[i,j]
        for j in range(A.shape[1]):
            ls_son_A.append(result)
        ls_A.append(ls_son_A)
    ls_B = []
    for i in range(0,B.shape[0]):
        result = 0
        ls_son_B = []
        for j in range(0,B.shape[1]):
            result = result + B[i,j]*B[i,j]
        for j in range(B.shape[1]):
            ls_son_B.append(result)
        ls_B.append(ls_son_B)
    matrix_A = np.matrix(ls_A)
    matrix_B = np.matrix(ls_B)

    print(matrix_A.shape)
    print(matrix_B.shape)

    distance = matrix_A + matrix_B - 2*ABT
    euclideanDistances = np.sqrt(distance)
    return euclideanDistances
def WKNN( file , m , k ):   #file为文件名：xxxx.xlsx , m为CSI矩阵
    list_last = []
    for i in os.listdir(data_directory):
        if i==file:
            continue
        else:
            data = pd.read_excel(data_directory + '\\' + i)
            mat = ( data.iloc[:,1:65] ).values
            matrix = np.mat(mat)
            # list_test = data.iloc[:, 1].tolist()
            # for j in range(0, 451):
            #     euclidean_distance = euclidean_distance + (ls[j] - list_test[j]) * (ls[j] - list_test[j])
            # euclidean_distance = math.sqrt(euclidean_distance)
            euclidean_distance = EuclideanDistances(m,matrix)
            list_last.append(euclidean_distance)
    list_last_copy = []
    for i in list_last:
        list_last_copy.append(i)
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
    list_table.remove(file)
    list_x = []
    list_y = []
    for i in list_index:
        data_name = list_table[i]
        data = pd.read_excel(data_directory + '\\' + data_name)
        x = data.iloc[0,65]
        y = data.iloc[0,66]
        list_x.append(x)
        list_y.append(y)
    sum_x = 0
    sum_y = 0
    coordinate = []
    for i in list_x:
        sum_x = sum_x + i
    for i in list_y:
        sum_y = sum_y + i
    coordinate_x = sum_x/len(list_x)
    coordinate_y = sum_y/len(list_y)
    coordinate.append(coordinate_x)
    coordinate.append(coordinate_y)
    return coordinate
# k = 2
# wknn_x = []
# wknn_y = []
# index = 1
#
# for i in os.listdir(r'C:\Users\Administrator\Desktop\CSI'):
#     print('---------------------WKNN' + str(index) + '处理完毕---------------------')
#
#     data = pd.read_excel(r'C:\Users\Administrator\Desktop\CSI' + '\\' + i)
#     m = ( data.iloc[:,1:65] ).values
#     mar = np.matrix(m)
#     coordinate = WKNN(i,mar,k)
#     wknn_x.append(coordinate[0])
#     wknn_y.append(coordinate[1])
#     print('---------------------WKNN' + str(index) + '处理完毕---------------------')
#     index = index + 1
#
# plt.plot(wknn_x,wknn_y)
# plt.show()
















