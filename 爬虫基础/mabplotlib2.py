'''
用matplotlib画三位圆锥，其解析式为z=-np.sqrt(x ** 2 + y ** 2)，
xy的范围都为[-5,5],步进0.5，
需要画出的要点为：标题，xy轴标签，三位平面，colorbar，色彩映射使用viridis
'''

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d

plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = ['SimHei']
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = np.arange(-5, 5, 0.5)
y = np.arange(-5, 5, 0.5)
x, y = np.meshgrid(x, y)
z=-np.sqrt(x ** 2 + y ** 2)

surf  = ax.plot_surface(x,y,z,
                        rstride = 1,
                        cstride= 1,
                        cmap = plt.get_cmap('viridis') )

plt.title("三维圆锥")
ax.set_xlabel("X_label");ax.set_ylabel("Y_label");ax.set_zlabel("Z_label")
fig.colorbar(surf,shrink=0.7,aspect=10)
plt.show()
