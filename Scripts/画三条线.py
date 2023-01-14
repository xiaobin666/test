import matplotlib.pyplot as plt
import pandas as pd
import os
import math

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
def hangdled_csi(str):
    str = delete_char(str,' ')
    if ( '+' in str ):
        index1 = last_char_index(str,'+')
    elif ( '-' in str ):
        index1 = last_char_index(str,'-')
    if 'i' in str:
        index2 = last_char_index(str, 'i')
        real_part = cut_char(str, 0, index1 - 1)
        imaginary_part = cut_char(str, index1 + 1, index2 - 1)
        result = float(real_part) * math.cos(float(imaginary_part))
    else:
        real_part = cut_char(str, 0, index1 - 1)
        imaginary_part = 0
        result = float(real_part) * math.cos(float(imaginary_part))
    return result
def change_number(ls):
    index = 0
    change_number = 0
    for i in range( len(ls)-1 ):
        if ls[index]>0:
            if ls[index+1]<0:
                change_number = change_number + 1
        else:
            if ls[index+1]>0:
                change_number = change_number + 1
        index = index + 1
    return change_number


for k in os.listdir(r'C:\Users\Administrator\Desktop\new_file'):
    index = 1
    data = pd.read_excel(r'C:\Users\Administrator\Desktop\new_file' + '\\' + k)
    ls_x = [ x for x in range(data.shape[0]) ]
    ls_min = []
    ls_max = []
    ls_change_number = []
    for i in range(0,data.shape[0]):
        ls_imaginary_part = []
        ls_real_part = []
        for j in range(2,66):
            csi = data.iloc[i, j]
            #去实部与虚部
            csi = delete_char(csi, ' ')
            if ('+' in csi):
                index1 = last_char_index(csi, '+')
                real_part = cut_char(csi, 0, index1 - 1)
            elif ('-' in csi):
                index1 = last_char_index(csi, '-')
                real_part = cut_char(csi, 0, index1 - 1)
            else:
                real_part = csi
            ls_real_part.append(real_part)

            if 'i' in csi:
                index2 = last_char_index(csi, 'i')
                imaginary_part = cut_char(csi, index1, index2 - 1)
                imaginary_part = float(imaginary_part)
            else:
                imaginary_part = 0
            ls_imaginary_part.append(imaginary_part)
        ls_real_part.sort()
        min_real_part = ls_real_part[0]
        max_real_part = ls_real_part[ len(ls_real_part)-1 ]
        min_real_part = float(min_real_part)
        max_real_part = float(max_real_part)
        ls_min.append(min_real_part)
        ls_max.append(max_real_part)
        num = change_number(ls_imaginary_part)
        ls_change_number.append(num)



    ax1 = plt.gca()
    ax1.plot(ls_x,ls_min,label = 'min',color = 'red')
    ax1.plot(ls_x,ls_max,label = 'max',color = 'blue')
    plt.xlabel('x')
    plt.ylabel('CSI')
    plt.legend()

    ax2 = ax1.twinx()
    ax2.set_ylabel('change_num')
    ax2.plot(ls_x,ls_change_number,label = 'change_num',color = 'black')

    plt.legend()
    plt.show()


#angle = []
# for i in range(0,451):
#     angle.append(i)
#未完
# for l in os.listdir(r'C:\Users\Administrator\Desktop\new_file'):
#     data = pd.read_excel(r'C:\Users\Administrator\Desktop\new_file' + '\\' + l)
#     data_angle = data.iloc[:, 0]
#     dataframe = pd.DataFrame()
#     dataframe.insert(0, 'Angle', angle)
#     for column in range(2, 66):
#         angle_index = 0
#         last_ls = []
#         realPart = []
#         imaginaryPart = []
#         for i in range(0, 451):
#             ls = []
#             flag = False
#             for j in data_angle:
#                 if j == i:
#                     ls.append(data.iloc[angle_index, column])
#                     angle_index = angle_index + 1
#                     flag = True
#                 else:
#                     if flag:
#                         break
#             if flag == False:
#                 ls.append(data.iloc[angle_index - 1, column])
#             sum = 0
#             for k in ls:
#                 #取实部
#                 # print(l)
#                 # print(k)
#                 csi = k
#                 csi = delete_char(csi, ' ')
#                 if ('+' in csi):
#                     index1 = last_char_index(csi, '+')
#                     real_part = cut_char(csi, 0, index1 - 1)
#                 elif ('-' in csi):
#                     index1 = last_char_index(csi, '-')
#                     real_part = cut_char(csi, 0, index1 - 1)
#                 else:
#                     real_part = csi
#                 #取虚部
#                 if 'i' in csi:
#                     index2 = last_char_index(csi, 'i')
#                     imaginary_part = cut_char(csi, index1, index2 - 1)
#                     imaginary_part = float(imaginary_part)
#                 else:
#                     imaginary_part = 0
#                 realPart.append(float(real_part))
#                 imaginaryPart.append(imaginary_part)
#             sum_real = 0
#             sum_imaginary = 0
#             for sum in realPart:
#                 sum_real = sum_real + sum
#             for sum in imaginaryPart:
#                 sum_imaginary = sum_imaginary + sum
#             result = str(sum_real/len(realPart)) + str(sum_imaginary/len(imaginaryPart)) + 'i'
#             last_ls.append(result)
#             dataframe.insert(column,'Csi'+str(column-1),last_ls)
#     x = data.iloc[1,68]
#     y = data.iloc[1,69]
#     X = [x]*451
#     Y = [y]*451
#     dataframe.insert(65,'X',X)
#     dataframe.insert(66,'Y',Y)
#
#     writer = pd.ExcelWriter(r"C:\Users\Administrator\Desktop\csi_average" + '\\' + l)
#     dataframe.to_excel(writer, index=False)
#     writer.save()
#     print('------------------------------' + l + '已生成------------------------------')

















