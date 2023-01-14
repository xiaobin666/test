import matplotlib.pyplot as plt
import matplotlib.ticker
import pandas as pd
import xlrd
import numpy as np
A=1
B=5
u=0
H=1
# x_last = -65
p_last = 100

# rss = [ -60, -60, -60, -60, -60, -60, -60, -60, -60, -60, -60, -60, -60, -60, -60, -60, -60,-60,-60,-60,
#     -60-0.05*1, -60-0.05*2, -60-0.05*3, -60-0.05*4, -60-0.05*5, -60-0.05*6, -60-0.05*7, -60-0.05*8, -60-0.05*9, -60-0.05*10, -60-0.05*11, -60-0.05*12, -60-0.05*13,
#     -60-0.05*14,
#     -60-0.05*15, -60-0.05*16, -60-0.05*17, -60-0.05*18, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71,
#     -71, -71, -71, -71, -71, -71,
#     -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71,
#     -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71,
#     -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71, -71,
#     -71+0.05*1, -71+0.05*2, -71+0.05*3, -71+0.05*4, -71+0.05*5, -71+0.05*6, -71+0.05*7, -71+0.05*8, -71+0.05*9, -71+0.05*10, -71+0.05*11, -71+0.05*12, -71+0.05*13, -71+0.05*14, -71+0.05*15,
#     -71+0.05*16, -71+0.05*17, -71+0.05*18, -71+0.05*19, -71+0.05*20, -71+0.05*21, -71+0.05*22, -65, -65, -63, -63, -63, -63, -63, -63, -63,
#     -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63,
#     -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63,
#     -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63,
#     -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63, -63,
#     -63-0.05*1, -63-0.05*2, -63-0.05*3, -63-0.05*4, -63-0.05*5, -63-0.05*6, -63-0.05*7, -63-0.05*8, -63-0.05*9, -63-0.05*10, -63-0.05*11, -63-0.05*12, -63-0.05*13,
#     -63-0.05*14, -63-0.05*15, -63-0.05*16, -63-0.05*17, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69,
#     -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69,
#     -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69,
#     -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69,
#     -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69, -69+0.5]

# num = 0
# for i in rss:
#     if i==-60:
#         num+=1
# print(num)

def kalman(z_measure,x_last,p_last, Q=0.1, R=10):
    x_mid = A*x_last + B*u
    p_mid = A*p_last*A + Q
    kg = p_mid*H/( H*p_mid*H + R)
    x_now = x_mid + kg*(z_measure - H*x_mid)
    p_now = (1-kg*H)*p_mid
    p_last = p_now
    x_last = x_now
    return x_now,p_last,x_last
file_fixed = r'C:\Users\Administrator\Desktop\SingleAPData\fixed\Table10.xlsx'
file_rotated = r'C:\Users\Administrator\Desktop\RSS\Table98.xlsx'

data1 = pd.read_excel(file_fixed)
data2 = pd.read_excel(file_rotated)
rss1 = data1.iloc[:,66]
rss2 = data2.iloc[:,1]
x1 = np.linspace(0, 6, len(rss1)).tolist()
x2 = np.linspace(0, len(rss2), len(rss2))
plt.figure(figsize=(10,4))
ax1 = plt.subplot(121)
ax2 = plt.subplot(122)
ax1.plot(x1,rss1,color = 'b')
ax1.set_xlabel('Time(s)')
ax1.set_ylabel('RSS(dB)')
ax1.set_title('Fixed antenna')

ax2.plot(x2,rss2,color = 'r')
ax2.set_xlabel('Angle(°)')
ax2.set_ylabel('RSS(dB)')
ax2.set_title('Rotated antenna')
ax2.xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(150))
plt.show()



# plt.figure(figsize=(10,4))
# ax1 = plt.subplot(121)
# ax2 = plt.subplot(122)
# data = xlrd.open_workbook(file_fixed)
# dataSheet = data.sheets()[0]
# list_actual = []
# list_predict = []
# firstValue = 0
# flag = 0
# for i in dataSheet.col_values(66):
#     if flag == 1:
#         firstValue = i
#         break
#     flag = flag + 1
# x_last = firstValue
# j = 0
# for i in dataSheet.col_values(66):
#     if (j > 0):
#         f = int(i)
#         list_actual.append(f)
#         x_predict, p_last, x_last = kalman(f, x_last, p_last)
#         list_predict.append(x_predict)
#     j = j + 1
# x = np.linspace(0, 6, len(list_actual)).tolist()
# y_actual = list_actual
# y_predict = list_predict
# ax1.plot(x,y_predict,color = 'b')
# ax1.set_xlabel('Time(s)')
# ax1.set_ylabel('RSS(dB)')
# ax1.set_title('Fixed antenna')
# ax1.set_xlim()
#
# firstValue = -60
# list_actual = []
# list_predict = []
# x_last = firstValue
# for i in rss:
#     list_actual.append(i)
#     x_predict, p_last, x_last = kalman(i, x_last, p_last)
#     list_predict.append(x_predict)
# x = np.linspace(0, len(list_actual), len(list_actual))
# y_predict = list_predict
#
#
# ax2.plot(x,y_predict,color = 'r')
# ax2.set_xlabel('Angle(°)')
# ax2.set_ylabel('RSS(dB)')
# ax2.set_title('Rotated antenna')
# ax2.xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(150))

# print(y_predict)
# # dataframe2 = pd.DataFrame()
# # dataframe2.insert(0,'Rotated antenna',y_predict)
# # dataframe1 = dataframe1.append(dataframe2)
# # writer = pd.ExcelWriter(r'C:\Users\Administrator\Desktop\painting.xlsx')
# # dataframe1.to_excel(writer, index=False)
# # writer.save()
# plt.show()













