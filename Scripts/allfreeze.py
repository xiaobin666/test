# 编写人：胡榕斌
# 专业：控制科学与工程
# 开发时间：2022/4/7 15:54
import pandas as pd
index_start = 1
index_end = 54
index = index_start
while ( index>=index_start and index<=index_end ):
    data = pd.read_excel(r'C:\Users\Administrator\Desktop\timerecord\allfreeze' + '\\' + 'Table' + str(index) + '.xlsx')
    dataframe = pd.DataFrame(data)
    list_angle = []
    for i in dataframe.iloc[:, 0].tolist():
        list_angle.append(0)
    dataframe = dataframe.drop(columns=['Angel'])
    dataframe.insert(0, 'Angel', list_angle)
    writer = pd.ExcelWriter(r"C:\Users\Administrator\Desktop\angle" + '\\' + 'Table' + str(index) + '.xlsx')
    dataframe.to_excel(writer, index=False)
    writer.save()
    print('------------------------------Table' + str(index) + '已生成------------------------------')
    index = index + 1