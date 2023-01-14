import pandas as pd
import os
angle = []
for i in range(0,451):
    angle.append(i)
for l in os.listdir(r'C:\Users\Administrator\Desktop\new_file'):
    data = pd.read_excel( r'C:\Users\Administrator\Desktop\new_file' + '\\' + l )
    X = [ data.iloc[0,68] ]*451
    Y = [ data.iloc[0,69] ]*451
    data_angle = data.iloc[:, 0].tolist()
    angle_index = 0
    last_ls = []
    last_ls_y = []

    index = 0
    for i in range(0, 451):
        ls = []
        ls_y = []
        if ( i in data_angle ):
            for j in data_angle:
                if j == i:
                    ls.append( data.iloc[angle_index, 67] )
                    ls_y.append( data.iloc[angle_index, 66] )
                    angle_index = angle_index + 1
        else:
            ls.append( last_ls[ len(last_ls)-1 ] )
            ls_y.append( last_ls_y[ len(last_ls_y)-1 ] )

        if l=='Table4.xlsx':
            print('--------------',index,'-------------------')
            print(ls)
            print(ls_y)
            print('--------------', index, '-------------------')
            index = index + 1
        sum = 0
        for k in ls:
            sum = sum + k
        average = round(sum / len(ls))
        last_ls.append(average)
        sum = 0
        for k in ls_y:
            sum = sum + k
        average = round(sum / len(ls_y))
        last_ls_y.append(average)

    dataframe = pd.DataFrame()
    dataframe.insert(0, 'Angle', angle)
    dataframe.insert(1, 'Rss', last_ls_y)
    dataframe.insert(2, 'FiltedRss', last_ls)
    dataframe.insert(3,'X',X)
    dataframe.insert(4,'Y',Y)
    writer = pd.ExcelWriter(r"C:\Users\Administrator\Desktop\RSS_unfilted" + '\\' + l)
    dataframe.to_excel(writer, index=False)
    writer.save()
    print( '------------------------------' + l + '已生成------------------------------')


