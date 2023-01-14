import os
import pandas as pd
import math
sigma = 100000
def Gaussian_function(x):
    left = 1/(math.sqrt(2*math.pi)*sigma)
    right = (math.e)**( (-x*x)/(2*sigma*sigma) )
    y = left*right
    return y
def Convolution_kernel(rss,step,index): #radius = 1,2,3
    data_index = []
    if index<step:
        for left in range(index):
            data_index.append(-(left+1))
    else:
        for left in range(step):
            data_index.append(-(left+1))
    data_index.append(0)
    if ( len(rss)-index-1 )<step:
        for right in range(len(rss)-index-1):
            data_index.append(right+1)
    else:
        for right in range(step):
            data_index.append(right+1)
    data_index.sort()
    data_kernel = []
    for i in data_index:
        data_kernel.append( Gaussian_function(i) )
    kernel_sum = sum(data_kernel)
    data_kernel_last = []
    for i in data_kernel:
        data_kernel_last.append( i/kernel_sum )
    return data_kernel_last
def Gaussianfilter(rss,index,step):  #radius = 1,2,3
    data = []
    if index < step:
        for left in range(index):
            data.append(rss[left])
        data.append(rss[index])
        for right in range(index + 1, step + index + 1):
            data.append(rss[right])
    elif (len(rss) - index - 1) < step:
        for left in range(index - step, index):
            data.append(rss[left])
        data.append(rss[index])
        for right in range(index + 1, len(rss)):
            data.append(rss[right])
    else:
        for left in range(index - step, index):
            data.append(rss[left])
        data.append(rss[index])
        for right in range(index + 1, step + index + 1):
            data.append(rss[right])
    convolution_kernel = Convolution_kernel(rss,step,index)
    data_number = 0
    for i in range(len(convolution_kernel)):
        data_number = data_number + data[i]*convolution_kernel[i]
    return data_number
def mean_filter(rss,index,step):
    data = []
    if index<step:
        for left in range(index):
            data.append(rss[left])
        data.append(rss[index])
        for right in range(index+1,step+index+1):
            data.append(rss[right])
    elif ( len(rss)-index-1 )<step:
        for left in range( abs(index-step) , index ):
            data.append(rss[left])
        data.append(rss[index])
        for right in range(index+1,len(rss)):
            data.append(rss[right])
    else:
        for left in range(abs(index-step),index):
            data.append(rss[left])
        data.append(rss[index])
        for right in range(index+1,step+index+1):
            data.append(rss[right])
    return sum(data)/len(data)
index = 0
for table in os.listdir(r'C:\Users\Administrator\Desktop\directional antenna\Data\HandledData\UnFilted'):
    data = pd.read_excel(r'C:\Users\Administrator\Desktop\directional antenna\Data\HandledData\UnFilted' + '\\' + table )
    X = data.iloc[:,5].tolist()
    Y = data.iloc[:,6].tolist()
    dataframe = pd.DataFrame()
    for column in range(0,5):
        rss = data.iloc[ :,column ].tolist()
        rss_meaned = []
        for i in range( len(rss) ):
            rss_meaned.append( mean_filter(rss,i,50) )
        rss_meaned_gaussianed = []
        for j in range( len(rss_meaned) ):
            rss_meaned_gaussianed.append( Gaussianfilter(rss_meaned,j,30) )
        dataframe.insert( column,'Direction'+str(column),rss_meaned_gaussianed )
    dataframe.insert( 5,'X',X )
    dataframe.insert( 6,'Y',Y )
    writer = pd.ExcelWriter(r'C:\Users\Administrator\Desktop\directional antenna\Data\HandledData\Mean(50)+Gauss(30)-Filter' + '\\' + table)
    dataframe.to_excel(writer, index=False)
    writer.save()
    print( '--------------------Table' + str(index) + '已生成--------------------' )
    index = index + 1



# import os
# import pandas as pd
# for table_index in range(0,59):
#     datafrane = pd.DataFrame()
#     index = 0
#     for direction_index in os.listdir(r'C:\Users\Administrator\Desktop\zhongjie'):
#         data = pd.read_excel(r'C:\Users\Administrator\Desktop\zhongjie' + '\\' + direction_index)
#         rss = data.iloc[:,table_index]
#         datafrane.insert( index,'Direction'+str(index),rss )
#         index = index + 1
#
#     if table_index!=0:
#         table_name = str(table_index) + '.xlsx'
#         Data = pd.read_excel( r'C:\Users\Administrator\Desktop\Summary\Data\HandledData\4AP\Mean(50)+Gauss(30)-Filter' + '\\' + table_name )
#         x = Data.iloc[1,5]
#         y = Data.iloc[1,6]
#         X = [ x ]*250
#         Y = [ y ]*250
#         datafrane.insert( 5,'X',X )
#         datafrane.insert( 6,'Y',Y )
#     writer = pd.ExcelWriter(r'C:\Users\Administrator\Desktop\directional antenna\Data\HandledData\UnFilted' + '\\' + 'Table' + str(table_index) + '.xlsx')
#     datafrane.to_excel(writer, index=False)
#     writer.save()




