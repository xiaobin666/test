import math
import matplotlib.pyplot as plt
import pandas as pd
A=1
B=5
u=0
H=1
# x_last = -65
p_last = 10
def kalman(z_measure,x_last,p_last, Q=0.1, R=20):
    x_mid = A*x_last + B*u
    p_mid = A*p_last*A + Q
    kg = p_mid*H/( H*p_mid*H + R)
    x_now = x_mid + kg*(z_measure - H*x_mid)
    p_now = (1-kg*H)*p_mid
    p_last = p_now
    x_last = x_now
    return x_now,p_last,x_last
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

data = pd.read_excel( r'D:\×ÀÃæ\rss.xlsx' )
rss = data.iloc[:,0].tolist()
# firstValue = data.iloc[0,1]
# x_last = firstValue
# list_predict = []
# for i in rss:
#     f = int(i)
#     x_predict, p_last, x_last = kalman(f, x_last, p_last)
#     list_predict.append(x_predict)
sigma = 100000
gaussianfiltered_rss = []
radius = 30
data_Gaussianfilter_rss = []
for index in range( len(rss) ):
    data_filted = Gaussianfilter(rss,index,radius)
    data_Gaussianfilter_rss.append(data_filted)

# data_Gaussianfilter_Kalman = []
# for index in range( len(rss) ):
#     # data_filted = Gaussianfilter(list_predict,index,radius)
#     data_Gaussianfilter_Kalman.append(data_filted)
#     index+=1

x = [ i for i in range(len(rss)) ]

plt.plot(x,rss,color='blue')
# plt.plot(x,list_predict,color='green')
plt.plot(x,data_Gaussianfilter_rss,color='red')
plt.show()

# dataframe = pd.DataFrame()
# dataframe.insert(0,'Kalman-RSS',list_predict)
# dataframe.insert(1,'RSS',rss)
# dataframe.insert(2,'Gaussianfilter-RSS',data_Gaussianfilter_rss)
# dataframe.insert(3,'Kalman+Gaussianfilter-RSS',data_Gaussianfilter_Kalman)
# writer = pd.ExcelWriter(r'C:\Users\Administrator\Desktop\data.xlsx')
# dataframe.to_excel(writer, index=False)
# writer.save()