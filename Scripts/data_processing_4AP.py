
import pandas as pd
import os
A = r'C:\Users\Administrator\Desktop\4AP\A'
B = r'C:\Users\Administrator\Desktop\4AP\B'
C = r'C:\Users\Administrator\Desktop\4AP\C'
D = r'C:\Users\Administrator\Desktop\4AP\D'
list = [ A,B,C,D ]
start = 1
end = 59
xlsx = start
list1 = ['A', 'B', 'C', 'D']
while (xlsx>=start) and (xlsx<=end):
    max_time = 0
    for i in list:
        for j in os.listdir(i):
            if j == ( str(xlsx) + '.xlsx' ):
                data = pd.read_excel(i+'\\'+j)
                time = data.iloc[ data.shape[0]-1 , 1 ]
                if time>max_time:
                    max_time = time
                    max_xlsx = i + '\\' + j
                break
    max_xlsx_data = pd.read_excel(max_xlsx)
    Time = max_xlsx_data.iloc[:,1].tolist()
    X = max_xlsx_data.iloc[:,68].tolist()
    Y = max_xlsx_data.iloc[:,69].tolist()
    dataframe = pd.DataFrame()
    for i in list:
        for j in os.listdir(i):
            if (str(xlsx)+'.xlsx') in os.listdir(i):
                if (i + '\\' + j) != max_xlsx:
                    if i == A:
                        rows = 0
                    elif i == B:
                        rows = 1
                    elif i == C:
                        rows = 2
                    elif i == D:
                        rows = 3
                    if j == str(xlsx) + '.xlsx':
                        data = pd.read_excel(i + '\\' + j)
                        rss_index = 0
                        RSS = []
                        for t in range(0, int(max_time) + 1):
                            max_num = 0
                            for l in max_xlsx_data.iloc[:, 1].tolist():
                                if (l >= t) and (l <= t + 1):
                                    max_num = max_num + 1
                                if l > (t + 1):
                                    break
                            num = 0
                            for d in data.iloc[:, 1].tolist():
                                if (d >= t) and (d <= t + 1):
                                    RSS.append(data.iloc[rss_index, 67])
                                    rss_index = rss_index + 1
                                    num = num + 1
                                    last_data = d
                                if d > (t + 1):
                                    break
                            if num < max_num:
                                # print(RSS)
                                # if len(RSS)!=0:
                                index = data.iloc[:, 1].tolist().index(last_data)
                                rss = data.iloc[index, 67]
                                for n in range(max_num):
                                    if num != max_num:
                                        RSS.append(rss)
                                        num = num + 1
                                    else:
                                        break
                                # else:
                                #     rss = data.iloc[0, 67]
                                #     for n in range(max_num):
                                #         if num != max_num:
                                #             RSS.append(rss)
                                #             num = num + 1
                                #         else:
                                #             break
                            else:
                                RSS = RSS[0:len(RSS) - (num - max_num)]
                        max_rows = max_xlsx_data.shape[0]
                        if len(RSS) < max_rows:
                            for o in range(max_rows):
                                if len(RSS) != max_rows:
                                    RSS.append(RSS[len(RSS) - 1])
                                else:
                                    break
                        elif len(RSS) == max_rows:
                            # print('---------===------------')
                            pass
                        elif len(RSS) > max_rows:
                            # print('--------->>------------')
                            pass
                        if rows == 0:
                            RSS0 = RSS.copy()
                        elif rows == 1:
                            RSS1 = RSS.copy()
                        elif rows == 2:
                            RSS2 = RSS.copy()
                        elif rows == 3:
                            RSS3 = RSS.copy()
                else:
                    if i == A:
                        rows = 0
                    elif i == B:
                        rows = 1
                    elif i == C:
                        rows = 2
                    elif i == D:
                        rows = 3
                    if j == str(xlsx) + '.xlsx':
                        data = pd.read_excel(i + '\\' + j)
                        RSS = data.iloc[:, 67].tolist()
                        if rows == 0:
                            RSS0 = RSS.copy()
                        elif rows == 1:
                            RSS1 = RSS.copy()
                        elif rows == 2:
                            RSS2 = RSS.copy()
                        elif rows == 3:
                            RSS3 = RSS.copy()
            else:
                if i == A:
                    rows = 0
                elif i == B:
                    rows = 1
                elif i == C:
                    rows = 2
                elif i == D:
                    rows = 3
                RSS = [0]*max_xlsx_data.shape[0]
                if rows == 0:
                    RSS0 = RSS.copy()
                elif rows == 1:
                    RSS1 = RSS.copy()
                elif rows == 2:
                    RSS2 = RSS.copy()
                elif rows == 3:
                    RSS3 = RSS.copy()
    dataframe.insert( 0,'Time',Time )
    dataframe.insert( 1,'RSS_A',RSS0 )
    dataframe.insert( 2,'RSS_B',RSS1 )
    dataframe.insert( 3,'RSS_C',RSS2 )
    dataframe.insert( 4,'RSS_D',RSS3 )
    dataframe.insert( 5,'X',X )
    dataframe.insert( 6,'Y',Y )
    writer = pd.ExcelWriter(r'C:\Users\Administrator\Desktop\4AP-data-first'+'\\'+str(xlsx)+'.xlsx')
    print('------------------'+str(xlsx)+'.xlsx'+'已生成------------------')
    xlsx = xlsx + 1
    dataframe.to_excel(writer,index=False)
    writer.save()









