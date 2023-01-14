
import pandas as pd
import math
import os
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
        imaginary_part = cut_char(str, index1 + 1, index2 - 1)

        real_part = float(real_part)
        imaginary_part = float(imaginary_part)

        result = a * math.sqrt( (real_part)**2 + imaginary_part**2 ) + b*imaginary_part
        # result = float(real_part) * math.cos(float(imaginary_part))
    else:
        real_part = cut_char(str, 0, index1 - 1)
        imaginary_part = 0

        result = a * math.sqrt((real_part) ** 2 + imaginary_part ** 2) + b * imaginary_part

        # result = float(real_part) * math.cos(float(imaginary_part))
    return result

# for k in os.listdir(r'C:\Users\Administrator\Desktop\new_file'):
#     data = pd.read_excel(r'C:\Users\Administrator\Desktop\new_file' + '\\' + k)
#     dataframe = pd.DataFrame()
#     Angle = data.iloc[:,0]
#     X = data.iloc[:,68]
#     Y = data.iloc[:,69]
#     dataframe.insert(0,'Angle',Angle)
#     for i in range(2,66):
#         list_csi = []
#         for j in range(data.shape[0]):
#             csi = hangdled_csi(data.iloc[j,i])
#             list_csi.append(csi)
#         dataframe.insert(i-1,'Csi'+str(i-1),list_csi)
#     dataframe.insert(65,'X',X)
#     dataframe.insert(66,'Y',Y)
#     writer = pd.ExcelWriter(r'C:\Users\Administrator\Desktop\handled_csi' + '\\' + k)
#     dataframe.to_excel(writer,index=False)
#     writer.save()
#     print('---------------------------------' + k + '已生成----------------------------------')
angle = []
for an in range(0,451):
    angle.append(an)
for l in os.listdir(r'C:\Users\Administrator\Desktop\handled_csi'):
    data = pd.read_excel( r'C:\Users\Administrator\Desktop\handled_csi' + '\\' + l )
    data_angle = data.iloc[:, 0]
    dataframe = pd.DataFrame()
    dataframe.insert(0, 'Angle', angle)
    for column in range(1,65):
        angle_index = 0
        last_ls = []
        for i in range(0, 451):
            ls = []
            flag = False
            for j in data_angle:
                if j == i:
                    ls.append(data.iloc[angle_index, column])
                    angle_index = angle_index + 1
                    flag = True
                else:
                    if flag:
                        break
            if flag==False:
                ls.append(data.iloc[angle_index - 1, column])
            if i==0:
                sum = 0
                for s in ls:
                    sum = sum + s
                average = sum/len(ls)
            else:
                if len(ls) > 1:
                    ls_new = []
                    angle_previous = last_ls[len(last_ls) - 1]
                    for a in ls:
                        ls_new.append(abs(a - angle_previous))
                    ls_new_copy = ls_new.copy()
                    ls_new_copy.sort()
                    index = ls_new.index(ls_new_copy[0])
                    average = ls[index]
                else:
                    average = ls[0]
            # sum = 0
            # for k in ls:
            #     sum = sum + k
            # average = (sum / len(ls))
            last_ls.append(average)
        dataframe.insert(column, 'Csi'+str(column), last_ls)
    x = data.iloc[1,65]
    y = data.iloc[1,66]
    X = []
    Y = []
    for i in range(451):
        X.append(x)
        Y.append(y)
    dataframe.insert(65,'X',X)
    dataframe.insert(66,'Y',Y)
    writer = pd.ExcelWriter(r"C:\Users\Administrator\Desktop\CSI" + '\\' + l)
    dataframe.to_excel(writer, index=False)
    writer.save()
    print( '------------------------------' + l + '已生成------------------------------')
