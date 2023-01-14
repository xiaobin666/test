
import pandas as pd
import os

directory = r'C:\Users\Administrator\Desktop\4AP-data-first'
max_rows = 0
for i in os.listdir(directory):
    data = pd.read_excel(directory + '\\' + i)
    rows = data.shape[0]
    if rows > max_rows:
        max_rows = rows
        max_xlsx = directory + '\\' + i
max_xlsx_data = pd.read_excel(max_xlsx)

Time = max_xlsx_data.iloc[:,0].tolist()
max_step = int( max_rows/5 )
list = [ 'A','B','C','D' ]
for i in os.listdir(directory):
    dataframe = pd.DataFrame()
    dataframe.insert(0, 'Time', Time)
    if ( directory+'\\'+i )!=max_xlsx:
        data = pd.read_excel( directory+'\\'+i )
        x = data.iloc[1,5]
        y = data.iloc[1,6]
        X = [x]*max_rows
        Y = [y]*max_rows
        for j in list:
            RSS_new = []
            if j=='A':
                RSSA = data.iloc[:,1].tolist()
                step = int( len(RSSA)/5 )
                for k in range(5):
                    RSS_lacked = RSSA[ k*step:(k+1)*step ]
                    while ( len(RSS_lacked)!=max_step ):
                        RSS_lacked.append( RSS_lacked[ len(RSS_lacked)-1 ] )
                    for l in RSS_lacked:
                        RSS_new.append(l)
                if len(RSS_new) != max_rows:
                    print('相差' + ':' + str(max_rows - len(RSS_new)))
                    while len(RSS_new) != max_rows:
                        RSS_new.append(RSS_new[len(RSS_new) - 1])
                dataframe.insert(1, 'RSS_A', RSS_new)
            elif j=='B':
                RSSB = data.iloc[:, 2].tolist()
                step = int(len(RSSB) / 5)
                for k in range(5):
                    RSS_lacked = RSSB[k * step:(k + 1) * step]
                    while (len(RSS_lacked) != max_step):
                        RSS_lacked.append(RSS_lacked[len(RSS_lacked) - 1])
                    for l in RSS_lacked:
                        RSS_new.append(l)
                if len(RSS_new) != max_rows:
                    print('相差' + ':' + str(max_rows - len(RSS_new)))
                    while len(RSS_new) != max_rows:
                        RSS_new.append(RSS_new[len(RSS_new) - 1])
                dataframe.insert(2, 'RSS_B', RSS_new)
            elif j=='C':
                RSSC = data.iloc[:, 3].tolist()
                step = int(len(RSSC) / 5)
                for k in range(5):
                    RSS_lacked = RSSC[k * step:(k + 1) * step]
                    while (len(RSS_lacked) != max_step):
                        RSS_lacked.append(RSS_lacked[len(RSS_lacked) - 1])
                    for l in RSS_lacked:
                        RSS_new.append(l)
                if len(RSS_new) != max_rows:
                    print('相差' + ':' + str(max_rows - len(RSS_new)))
                    while len(RSS_new) != max_rows:
                        RSS_new.append(RSS_new[len(RSS_new) - 1])
                dataframe.insert(3, 'RSS_C', RSS_new)
            elif j=='D':
                RSSD = data.iloc[:, 4].tolist()
                step = int(len(RSSD) / 5)
                for k in range(5):
                    RSS_lacked = RSSD[k * step:(k + 1) * step]
                    while (len(RSS_lacked) != max_step):
                        RSS_lacked.append(RSS_lacked[len(RSS_lacked) - 1])
                    for l in RSS_lacked:
                        RSS_new.append(l)
                if len(RSS_new) != max_rows:
                    print('相差' + ':' + str(max_rows - len(RSS_new)))
                    while len(RSS_new) != max_rows:
                        RSS_new.append(RSS_new[len(RSS_new) - 1])
                dataframe.insert(4, 'RSS_D', RSS_new)
        dataframe.insert(5,'X',X)
        dataframe.insert(6,'Y',Y)
    else:
        data = pd.read_excel( max_xlsx )
        dataframe = pd.DataFrame(data)
    writer = pd.ExcelWriter(r'C:\Users\Administrator\Desktop\4AP-data-second' + '\\' + i)
    print('------------------' + i +  '已生成------------------')
    dataframe.to_excel(writer, index=False)
    writer.save()



































































