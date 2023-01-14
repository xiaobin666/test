import matplotlib.pyplot as plt
import pandas as pd
def mean_filter(rss,index,step):
    data = []
    if index<step:
        for left in range(index):
            data.append(rss[left])
        data.append(rss[index])
        for right in range(index+1,step+index+1):
            data.append(rss[right])
    elif ( len(rss)-index-1 )<step:
        for left in range(index-step,index):
            data.append(rss[left])
        data.append(rss[index])
        for right in range(index+1,len(rss)):
            data.append(rss[right])
    else:
        for left in range(index-step,index):
            data.append(rss[left])
        data.append(rss[index])
        for right in range(index+1,step+index+1):
            data.append(rss[right])
    return sum(data)/len(data)

file = pd.read_excel(r'D:\×ÀÃæ\RSS-data\SingleAP\HandleData\Table4.xlsx')
data = file.iloc[:,1].tolist()
data_mean_filter = []
for i in range(len(data)):
    mean_filter_num = mean_filter(data,i,100)
    data_mean_filter.append(mean_filter_num)

x = [ i for i in range(len(data)) ]
plt.plot(x,data,color='b')
plt.plot(x,data_mean_filter,color='r')
plt.show()



xlsx = pd.DataFrame()
xlsx.insert(0,'RSS',data_mean_filter)

writer = pd.ExcelWriter(r'D:\×ÀÃæ\rss.xlsx')
xlsx.to_excel(writer, index=False)
writer.save()