# 编写人：胡榕斌
# 专业：控制科学与工程
# 开发时间：2022/1/13 17:11
import numpy as np


def get_D(ob_list):
    sz = len(ob_list)
    s = 0
    for i in range(0, sz):
        s = s + ob_list[i]
    avg = s / sz
    s1 = 0
    for i in range(0, sz):
        s1 = s1 + (ob_list[i] - avg) ** 2
    s2 = np.sqrt(s1 / sz)
    return s2
