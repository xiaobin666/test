
import pandas as pd
import os
def insert_rows(df,ls):
    df_new = pd.concat([df,ls],ignore_index=True)
    return df_new
data_directory = r'C:\Users\Administrator\Desktop\new_file'
Angle = [ x for x in range(451) ]
for table in os.listdir(data_directory):
    data = pd.read_excel( data_directory+'\\'+table )
    x = data.iloc[1,68]
    y = data.iloc[1,69]
    X = [x]*451
    Y = [y]*451
    index = 0
    for angle in range(451):
        if index == 0:
            df = data.iloc[index:index + 1, 2:66]
            df2 = data.iloc[index:index + 1, 2:66]
            index = index + 1
            continue
        else:
            if angle in data.iloc[:,0].tolist():
                angle_index = data.iloc[:, 0].tolist().index(angle)
                df2 = data.iloc[angle_index:angle_index+1,2:66]
                df = insert_rows(df,df2)
            else:
                df = insert_rows(df,df2)
    dataframe = pd.DataFrame(df)
    dataframe.insert(0,'Angle',Angle)
    dataframe.insert(65,'X',X)
    dataframe.insert(66,'Y',Y)
    writer = pd.ExcelWriter(r'C:\Users\Administrator\Desktop\CSI_conplex' + '\\' + table)
    df.to_excel(writer, index=False)
    writer.save()
    print('---------------------------------' + table + '已生成----------------------------------')
