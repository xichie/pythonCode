# coding: utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('./类别数与最大熵之间的关系R.xlsx',skiprows=0, index_col=0, skip_footer=0)
ax = data.plot(xlim=(2, 20), legend=None)
ax.set_ylabel('The maximum of entropy')
# 保存图像
fig = ax.get_figure()
fig.savefig('./类与熵关系图.jpg')

