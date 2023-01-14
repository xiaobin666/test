import os

import xlrd
import numpy as np
import matplotlib.pyplot as plt
import keyboard
import pandas as pd

A=1
B=5
u=0
H=1
# x_last = -65
p_last = 10
def kalman(z_measure,x_last,p_last, Q=0.1, R=15000):
    x_mid = A*x_last + B*u
    p_mid = A*p_last*A + Q
    kg = p_mid*H/( H*p_mid*H + R)
    x_now = x_mid + kg*(z_measure - H*x_mid)
    p_now = (1-kg*H)*p_mid
    p_last = p_now
    x_last = x_now
    return x_now,p_last,x_last

ls = [ 'RSS_A','RSS_B','RSS_C','RSS_D' ]
for table in os.listdir(r'C:\Users\Administrator\Desktop\RSS-data\4AP\HandleData\UnFilted'):
    data_name = r'C:\Users\Administrator\Desktop\RSS-data\4AP\HandleData\UnFilted'+'\\'+table
    Data = pd.read_excel(data_name)
    data = xlrd.open_workbook(data_name)
    dataSheet = data.sheets()[0]
    dataframe = pd.DataFrame()
    Time = Data.iloc[:,0].tolist()
    dataframe.insert(0,'Time',Time)
    for column_index in range(1,5):
        list_predict = []
        list_actual = Data.iloc[:,column_index].tolist()

        sum = 0
        for i in list_actual:
            sum += i
        average = sum / len(list_actual)
        firstValue = average
        x_last = firstValue
        j = 0
        for i in dataSheet.col_values(column_index):
            if (j > 0):
                f = int(i)
                x_predict, p_last, x_last = kalman(f, x_last, p_last)
                list_predict.append(x_predict)
            j = j + 1
        x = np.linspace(0, len(list_actual), len(list_actual))
        y_actual = list_actual
        y_predict = list_predict
        rounded_list = []
        for i in list_predict:
            rounded_list.append(round(i))
        # plt.plot(x, y_actual, color='red')
        # plt.plot(x, y_predict, color='blue')
        # plt.plot(x,rounded_list,color = 'black')
        # plt.xlabel('x', size=14)
        # plt.ylabel("RSS", size=14)
        # # plt.title('Compare')
        # plt.title(table)
        # plt.legend(["ActualValue", "FiltedValue", "roundedValue"])
        # plt.show()
        dataframe.insert( column_index,ls[column_index-1],rounded_list )
    X = Data.iloc[:,5].tolist()
    Y = Data.iloc[:,6].tolist()
    dataframe.insert(5,'X',X)
    dataframe.insert(6,'Y',Y)
    writer = pd.ExcelWriter(r'C:\Users\Administrator\Desktop\RSS-data\4AP\HandleData\Filted'+'\\'+table)
    dataframe.to_excel(writer, index=False)
    writer.save()















