# 编写人：胡榕斌
# 专业：控制科学与工程
# 开发时间：2022/4/5 21:26

import pandas as pd
def count_char(str, char, index):
    count = 0
    cishu = 0
    str = list(str)
    for i in str:
        if i == char:
            cishu += 1
        if cishu == index:
            return count
        count = count + 1
def delete_char(str, char):
    s = ''
    for i in list(str):
        if i == char or i==' ' :
            continue
        s = s + i
    return s

txt_start = 1
txt_end = 50
txt = txt_start

xlsx_start =221
xlsx_end =270
xlsx = xlsx_start
index = 0
while ( xlsx>=xlsx_start and xlsx<=xlsx_end ):
    data_txt_total = r'C:\Users\Administrator\Desktop\timerecord\moving\gdabcde\gdabcde.txt'
    data_txt = r'C:\Users\Administrator\Desktop\timerecord\moving\gdabcde' + '\\' + str(txt) + '.txt'
    data_xlsx = r'C:\Users\Administrator\Desktop\timerecord\moving\gdabcde' + '\\' + 'Table' + str(xlsx) + '.xlsx'
    data_time = pd.read_csv(data_txt_total, encoding="ANSI", header=None)
    data_time_filted = pd.read_csv(data_txt, header=None)
    data_table = pd.read_excel(data_xlsx)
    dataframe = pd.DataFrame(data_table)
    start_time = data_time.iloc[index, 0]
    end_time = data_time.iloc[index+1, 0]
    space_index_start = count_char(start_time, " ", 2)
    space_index_end = count_char(end_time, ' ', 3)
    index_start = 0
    string_start = ""
    for i in list(start_time):
        if (index_start > space_index_start):
            string_start = string_start + i
        index_start = index_start + 1
    index_end = 0
    string_end = ""
    for i in list(end_time):
        if (index_end > space_index_end):
            string_end = string_end + i
        index_end = index_end + 1
    string_start = float(delete_char(string_start, ':'))
    string_end = float(delete_char(string_end, ':'))
    list_filted_time = []
    index_space = 1
    for i in data_time_filted.iloc[:, 0]:
        if index_space < 10:
            b = count_char(i, ' ', 7)
        elif (index_space >= 10 and index_space < 100):
            b = count_char(i, ' ', 6)
        elif index_space >= 100 and index_space<1000:
            b = count_char(i, ' ', 5)
        elif index_space>=1000:
            b = count_char(i, ' ', 4)
        index_filted = 0
        string_filted = ''
        for i in i:
            if index_filted > b:
                string_filted = string_filted + i
            index_filted = index_filted + 1
        c = float(delete_char(string_filted, ':'))
        index_space = index_space + 1
        list_filted_time.append(c)
    index_deteled = 0
    deleted = []
    for i in list_filted_time:
        if (i < string_start or i > string_end):
            deleted.append(index_deteled)
        index_deteled = index_deteled + 1
    for i in deleted:
        dataframe = dataframe.drop(i)
    l = []
    for i in dataframe.iloc[:, 1]:
        l.append(i)
    index_time = 0
    list_time = []
    for i in dataframe.iloc[:, 1]:
        if index_time == 0:
            f = 0
            list_time.append(f)
            index_time = index_time + 1
            continue
        f = f + (l[index_time] - l[index_time - 1])
        index_time = index_time + 1
        list_time.append(f)
    dataframe = dataframe.drop(columns=['Time'])
    dataframe.insert(1, 'Time', list_time)
    list_time = dataframe.iloc[:, 1].tolist()
    list_0_15 = []
    list_2_35 = []
    list_4_55 = []
    list_6_75 = []
    list_8_95 = []
    for i in list_time:
        if (i >= 0 and i <= 1.5):
            list_0_15.append(i)
        elif (i > 2 and i <= 3.5):
            list_2_35.append(i)
        elif (i > 4 and i <= 5.5):
            list_4_55.append(i)
        elif (i > 6 and i <= 7.5):
            list_6_75.append(i)
        elif (i > 8 and i <= 9.5):
            list_8_95.append(i)
    index_angle = 0
    list_angle = []
    for i in list_time:
        if index_angle == 0:
            angle = 0
            list_angle.append(angle)
            index_angle = index_angle + 1
            continue
        if (i >= 0 and i <= 1.5):
            length = len(list_0_15)
            step = 90 / length
            angle = angle + step
            list_angle.append( round(angle) )
        elif (i > 1.5 and i <= 2.0):
            angle = 90
            list_angle.append(angle)
        elif (i > 2 and i <= 3.5):
            length = len(list_2_35)
            step = 90 / length
            angle = angle + step
            list_angle.append( round(angle) )
        elif (i > 3.5 and i <= 4.0):
            angle = 180
            list_angle.append(angle)
        elif (i > 4 and i <= 5.5):
            length = len(list_4_55)
            step = 90 / length
            angle = angle + step
            list_angle.append( round(angle) )
        elif (i > 5.5 and i <= 6.0):
            angle = 270
            list_angle.append(angle)
        elif (i > 6 and i <= 7.5):
            length = len(list_6_75)
            step = 90 / length
            angle = angle + step
            list_angle.append( round(angle) )
        elif (i > 7.5 and i <= 8.0):
            angle = 360
            list_angle.append(angle)
        elif (i > 8 and i <= 9.5):
            length = len(list_8_95)
            step = 90 / length
            angle = angle + step
            list_angle.append( round(angle) )
        elif i > 9.5:
            angle = 450
            list_angle.append(angle)
    dataframe = dataframe.drop(columns=['Angel'])
    dataframe.insert(0, 'Angel', list_angle)
    index = index + 2
    writer = pd.ExcelWriter( r"C:\Users\Administrator\Desktop\新建文件夹 (2)" + '\\' + 'Table' + str(xlsx) + '.xlsx' )
    dataframe.to_excel(writer, index=False)
    writer.save()
    print('------------------------------Table' + str(xlsx) + '已生成------------------------------')
    xlsx = xlsx + 1
    txt = txt + 1
    # if xlsx==38 :
    #     xlsx = xlsx + 1
    #     txt = txt + 1
    #     index = index + 2
    # if xlsx==71:
    #     xlsx = xlsx + 2
    #     txt = txt + 2
    #     index = index + 4