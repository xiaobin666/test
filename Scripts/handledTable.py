
import pandas as pd
import numpy as np
import os

def insert_rows(df,ls):
    df_new = pd.concat([df,ls],ignore_index=True)
    return df_new

xlsx_550 = pd.read_excel(r'C:\Users\Administrator\Desktop\SingleAPData\rotating\Table550.xlsx')
list0_1 = []
list1_2 = []
list2_3 = []
list3_4 = []
list4_5 = []
list5_6 = []
list6_7 = []
list7_8 = []
list8_9 = []
list9_10 = []
list10_11 = []
for i in xlsx_550.iloc[:,1]:
    if ( i>=0 and i<=1 ):
        list0_1.append(i)
    elif ( i>1 and i<=2 ):
        list1_2.append(i)
    elif ( i>2 and i<=3 ):
        list2_3.append(i)
    elif ( i>3 and i<=4 ):
        list3_4.append(i)
    elif ( i>4 and i<=5 ):
        list4_5.append(i)
    elif ( i>5 and i<=6 ):
        list5_6.append(i)
    elif ( i>6 and i<=7 ):
        list6_7.append(i)
    elif ( i>7 and i<=8 ):
        list7_8.append(i)
    elif ( i>8 and i<=9 ):
        list8_9.append(i)
    elif ( i>9 and i<=10 ):
        list9_10.append(i)
    elif ( i>10 and i<=11 ):
        list10_11.append(i)
data_directory = r'C:\Users\Administrator\Desktop\new_file'
for i in os.listdir(data_directory):
    num0_1 = 0
    num1_2 = 0
    num2_3 = 0
    num3_4 = 0
    num4_5 = 0
    num5_6 = 0
    num6_7 = 0
    num7_8 = 0
    num8_9 = 0
    num9_10 = 0
    num10_11 = 0
    data_file = data_directory + '\\' + i
    data = pd.read_excel(data_file)
    for j in data.iloc[:,1]:
        if (j >= 0 and j <= 1):
            num0_1 = num0_1 + 1
        elif (j > 1 and j <= 2):
            num1_2 = num1_2 + 1
        elif (j > 2 and j <= 3):
            num2_3 = num2_3 + 1
        elif (j > 3 and j <= 4):
            num3_4 = num3_4 + 1
        elif (j > 4 and j <= 5):
            num4_5 = num4_5 + 1
        elif (j > 5 and j <= 6):
            num5_6 = num5_6 + 1
        elif (j > 6 and j <= 7):
            num6_7 = num6_7 + 1
        elif (j > 7 and j <= 8):
            num7_8 = num7_8 + 1
        elif (j > 8 and j <= 9):
            num8_9 = num8_9 + 1
        elif (j > 9 and j <= 10):
            num9_10 = num9_10 + 1
        elif (j > 10 and j <= 11):
            num10_11= num10_11 + 1
    if num0_1<len(list0_1):
        dataframe0_1 = data.iloc[:num0_1,:]
        nearest_num = data.iloc[(num0_1-1),67]
        ls = [nearest_num]*(len(list0_1)-num0_1)
        dataframe = pd.DataFrame({'FiltedRss':ls})
        df0_1 = insert_rows(dataframe0_1,dataframe)
    if num1_2<len(list1_2):
        dataframe1_2 = data.iloc[num0_1:(num0_1+num1_2),:]
        nearest_num = data.iloc[(num0_1+num1_2 - 1), 67]
        ls = [nearest_num]*(len(list1_2)-num1_2)
        dataframe = pd.DataFrame({'FiltedRss':ls})
        df1_2 = insert_rows(dataframe1_2,dataframe)
    if num2_3<len(list2_3):
        dataframe2_3 = data.iloc[(num0_1+num1_2):(num0_1+num1_2+num2_3),:]
        nearest_num = data.iloc[(num0_1+num1_2+num2_3 - 1), 67]
        ls = [nearest_num]*(len(list2_3)-num2_3)
        dataframe = pd.DataFrame({'FiltedRss':ls})
        df2_3 = insert_rows(dataframe2_3,dataframe)
    if num3_4<len(list3_4):
        dataframe3_4 = data.iloc[(num0_1+num1_2+num2_3):(num0_1+num1_2+num2_3+num3_4),:]
        nearest_num = data.iloc[(num0_1+num1_2+num2_3+num3_4 - 1), 67]
        ls = [nearest_num]*(len(list3_4)-num3_4)
        dataframe = pd.DataFrame({'FiltedRss':ls})
        df3_4 = insert_rows(dataframe3_4,dataframe)
    if num4_5<len(list4_5):
        dataframe4_5 = data.iloc[(num0_1+num1_2+num2_3+num3_4):(num0_1+num1_2+num2_3+num3_4+num4_5),:]
        nearest_num = data.iloc[(num0_1+num1_2+num2_3+num3_4+num4_5 - 1), 67]
        ls = [nearest_num]*(len(list4_5)-num4_5)
        dataframe = pd.DataFrame({'FiltedRss':ls})
        df4_5 = insert_rows(dataframe4_5,dataframe)
    if num5_6<len(list5_6):
        dataframe5_6 = data.iloc[(num0_1+num1_2+num2_3+num3_4+num4_5):(num0_1+num1_2+num2_3+num3_4+num4_5+num5_6),:]
        nearest_num = data.iloc[(num0_1+num1_2+num2_3+num3_4+num4_5+num5_6 - 1), 67]
        ls = [nearest_num]*(len(list5_6)-num5_6)
        dataframe = pd.DataFrame({'FiltedRss':ls})
        df5_6 = insert_rows(dataframe5_6,dataframe)
    if num6_7<len(list6_7):
        dataframe6_7 = data.iloc[(num0_1+num1_2+num2_3+num3_4+num4_5+num5_6):(num0_1+num1_2+num2_3+num3_4+num4_5+num5_6+num6_7),:]
        nearest_num = data.iloc[(num0_1+num1_2+num2_3+num3_4+num4_5+num5_6+num6_7 - 1), 67]
        ls = [nearest_num]*(len(list6_7)-num6_7)
        dataframe = pd.DataFrame({'FiltedRss':ls})
        df6_7 = insert_rows(dataframe6_7,dataframe)
    if num7_8<len(list7_8):
        dataframe7_8 = data.iloc[(num0_1+num1_2+num2_3+num3_4+num4_5+num5_6+num6_7):(num0_1+num1_2+num2_3+num3_4+num4_5+num5_6+num6_7+num7_8),:]
        nearest_num = data.iloc[(num0_1+num1_2+num2_3+num3_4+num4_5+num5_6+num6_7+num7_8 - 1), 67]
        ls = [nearest_num]*(len(list7_8)-num7_8)
        dataframe = pd.DataFrame({'FiltedRss':ls})
        df7_8 = insert_rows(dataframe7_8,dataframe)
    if num8_9<len(list8_9):
        dataframe8_9 = data.iloc[(num0_1+num1_2+num2_3+num3_4+num4_5+num5_6+num6_7+num7_8):(num0_1+num1_2+num2_3+num3_4+num4_5+num5_6+num6_7+num7_8+num8_9),:]
        nearest_num = data.iloc[(num0_1+num1_2+num2_3+num3_4+num4_5+num5_6+num6_7+num7_8+num8_9 - 1), 67]
        ls = [nearest_num]*(len(list8_9)-num8_9)
        dataframe = pd.DataFrame({'FiltedRss':ls})
        df8_9 = insert_rows(dataframe8_9,dataframe)
    if num9_10<len(list9_10):
        dataframe9_10 = data.iloc[(num0_1+num1_2+num2_3+num3_4+num4_5+num5_6+num6_7+num7_8+num8_9):(num0_1+num1_2+num2_3+num3_4+num4_5+num5_6+num6_7+num7_8+num8_9+num9_10),:]
        nearest_num = data.iloc[(num0_1+num1_2+num2_3+num3_4+num4_5+num5_6+num6_7+num7_8+num8_9+num9_10 - 1), 67]
        ls = [nearest_num]*(len(list9_10)-num9_10)
        dataframe = pd.DataFrame({'FiltedRss':ls})
        df9_10 = insert_rows(dataframe9_10,dataframe)
    if num10_11<len(list10_11):
        dataframe10_11 = data.iloc[(num0_1+num1_2+num2_3+num3_4+num4_5+num5_6+num6_7+num7_8+num8_9+num9_10):(num0_1+num1_2+num2_3+num3_4+num4_5+num5_6+num6_7+num7_8+num8_9+num9_10+num10_11),:]
        nearest_num = data.iloc[(num0_1+num1_2+num2_3+num3_4+num4_5+num5_6+num6_7+num7_8+num8_9+num9_10+num10_11 - 1), 67]
        ls = [nearest_num]*(len(list10_11)-num10_11)
        dataframe = pd.DataFrame({'FiltedRss':ls})
        df10_11 = insert_rows(dataframe10_11,dataframe)
    df = pd.concat([df0_1,df1_2,df2_3,df3_4,df4_5,df5_6,df6_7,df7_8,df8_9,df9_10,df10_11],ignore_index=True)
    writer = pd.ExcelWriter(r'C:\Users\Administrator\Desktop\RSS_unfilted' + '\\' + i)
    df.to_excel(writer, index=False)
    writer.save()
    print('---------------------------------' + i + '已生成----------------------------------')