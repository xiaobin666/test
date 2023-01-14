# 编写人：胡榕斌
# 专业：控制科学与工程
# 开发时间：2022/3/25 15:12


import pandas as pd

coordinate_name = r"C:\Users\Administrator\Desktop\zuobiao.xls"
data_coordinate = pd.read_excel(coordinate_name)

coordinate_X= []
for i in data_coordinate['X']:
    coordinate_X.append(i)
coordinate_Y = []
for i in data_coordinate['Y']:
    coordinate_Y.append(i)

num = 1
table_totalNumber = 54

while num<=table_totalNumber:
    data_name = r"C:\Users\Administrator\Desktop\allfreeze\Table" + str(num) + ".xlsx"
    data_table = pd.read_excel(data_name)
    data_frame = pd.DataFrame(data_table)

    x1 = []
    y1 = []
    for i in range(0, data_table.shape[0]):
        x1.append(coordinate_X[num-1])
        y1.append(coordinate_Y[num-1])

    data_frame.insert(67, 'X', x1)
    data_frame.insert(68, 'Y', y1)

    writer = pd.ExcelWriter(r"C:\Users\Administrator\Desktop\test2\Table" + str(num) + ".xlsx")
    data_frame.to_excel(writer, index=False)
    writer.save()
    print('-----------------------Table' +  str(num) + '坐标已填充--------------------------')
    num = num + 1