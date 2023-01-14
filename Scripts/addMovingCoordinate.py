# 编写人：胡榕斌
# 专业：控制科学与工程
# 开发时间：2022/3/25 16:07


import pandas as pd

coordinate_name = r"C:\Users\Administrator\Desktop\zuobiao.xls"
data_coordinate = pd.read_excel(coordinate_name)
data_coordinateX= data_coordinate['X']
data_coordinateY= data_coordinate['Y']

coordinate_X = data_coordinateX.values.tolist()
coordinate_Y = data_coordinateY.values.tolist()


table_num = 1
table_totalNumber = 540
num = 0
while table_num<=table_totalNumber:
    data_name = r"C:\Users\Administrator\Desktop\allmoving\Table" + str(table_num) + ".xlsx"
    data_table = pd.read_excel(data_name)
    data_frame = pd.DataFrame(data_table)
    x1 = []
    y1 = []
    x1 = [ coordinate_X[num] ] * data_table.shape[0]
    y1 = [ coordinate_Y[num] ] * data_table.shape[0]

    data_frame.insert(68, 'X', x1)
    data_frame.insert(69, 'Y', y1)

    writer = pd.ExcelWriter(r"C:\Users\Administrator\Desktop\test\Table" + str(table_num) + ".xlsx")
    data_frame.to_excel(writer, index=False)
    writer.save()
    print('-----------------------Table' +  str(table_num) + '坐标已填充--------------------------')
    if table_num%10==0:
        num = num +1
    table_num = table_num + 1