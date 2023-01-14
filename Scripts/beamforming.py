# 编写人：胡榕斌
# 专业：控制科学与工程
# 开发时间：2022/3/25 20:36

import matplotlib.pyplot as plt
import math
import numpy as np

sita0 = 50
sita0_rand = sita0*math.pi/180
f = 1000
c = 1500
lamuda = c/f
d = lamuda/3
n = 10
fai =  ( 2*math.pi*d*math.sin(sita0_rand) )/lamuda
sita = np.linspace( -180 , 180 , 3600 ).tolist()
F = []
for i in sita:
    f1 = (n / 2) * ( 2 * math.pi * d * math.sin(i*math.pi/180) - fai)
    F1 = math.sin(f1)
    f2 = (1 / 2) * ( 2 * math.pi * d * math.sin(i*math.pi/180) - fai)
    F2 = math.sin(f2)
    F3 = (1/n)*(F1/F2)
    F4 = abs(F3)
    F.append(F4)
plt.plot(sita,F)
plt.show()