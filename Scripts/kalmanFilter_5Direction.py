import os
import matplotlib.pyplot as plt
import pandas as pd
A=1
B=5
u=0
H=1
x_last = -65
p_last = 10
def kalman(z_measure,x_last,p_last, Q=0.1, R=300):
    x_mid = A*x_last + B*u
    p_mid = A*p_last*A + Q
    kg = p_mid*H/( H*p_mid*H + R)
    x_now = x_mid + kg*(z_measure - H*x_mid)
    p_now = (1-kg*H)*p_mid
    p_last = p_now
    x_last = x_now
    return x_now,p_last,x_last
for table_name in os.listdir(r'C:\Users\Administrator\Desktop\directional antenna\Data\HandledData\UnFilted'):
    data = pd.read_excel( r'C:\Users\Administrator\Desktop\directional antenna\Data\HandledData\UnFilted' + '\\' + table_name )
    x = [ i for i in range(250) ]
    dataframe = pd.DataFrame()
    X = [ data.iloc[1,5] ]*250
    Y = [ data.iloc[1,6] ]*250
    for column in range(5):
        rss = data.iloc[:,column].tolist()
        firstValue = sum(rss)/len(rss)
        x_last = firstValue
        rss_filted = []
        for i in rss:
            rss_predict, p_last, x_last = kalman(i, x_last, p_last)
            rss_filted.append(rss_predict)
        rss_last = []
        for i in rss_filted:
            rss_last.append(round(i))
        plt.plot( x,rss,color='red' )
        plt.plot( x,rss_last,color='blue' )
        plt.xlabel('x',size=14)
        plt.ylabel('RSS',size=14)
        title = table_name + '  Direction' + str(column)
        plt.title( title )
        plt.legend( ['ActualValue','FiltedValue'] )
        dataframe.insert( column,'Direction'+str(column),rss_last )
        # plt.show()
    dataframe.insert( 5,'X',X )
    dataframe.insert( 6,'Y',Y )
    writer = pd.ExcelWriter(r"C:\Users\Administrator\Desktop\directional antenna\Data\HandledData\UnFilted" + '\\' + table_name)
    dataframe.to_excel(writer, index=False)
    writer.save()











