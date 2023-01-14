# 编写人：胡榕斌
# 专业：控制科学与工程
# 开发时间：2022/4/12 18:56
import pandas as pd
def delete_char(str,char):
    str = list(str)
    new_str = ''
    for i in str:
        if i==char:
            continue
        new_str = new_str + i
    return new_str
xlsx_start = 1
xlsx_end = 54
xlsx = xlsx_start
while ( xlsx>=xlsx_start and xlsx<=xlsx_end ):
    data_name = r'C:\Users\Administrator\Desktop\timerecord\allfreeze' + '\\' + 'Table' + str(xlsx) + '.xlsx'
    data = pd.read_excel(data_name)
    dataframe = pd.DataFrame(data)
    index_row = 0
    for i in range(dataframe.shape[0]):
        zero_number = 0
        list1 = []
        for j in data.iloc[index_row, 2:66].tolist():
            list1.append(j)
        for k in list1:
            k = delete_char(k, 'i')
            k = delete_char(k, ' ')
            k = delete_char(k, '.')
            k = delete_char(k, '+')
            k = delete_char(k, '-')
            k = int(k)
            if k == 0:
                zero_number = zero_number + 1
        if zero_number == 64:
            dataframe = dataframe.drop(index_row)
        index_row = index_row + 1
    writer = pd.ExcelWriter(r'C:\Users\Administrator\Desktop\新建文件夹 (2)' + '\\' + 'Table' + str(xlsx) + '.xlsx')
    dataframe.to_excel(writer, index=False)
    writer.save()
    print('---------------------------------Table' + str(xlsx) + '已生成---------------------------------')
    xlsx = xlsx + 1