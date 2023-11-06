import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']
data = np.random.randn(1000)

mu=data.mean()
sigma=data.std()

x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)

plt.plot(x, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp(- (x - mu)**2 / (2 * sigma**2)),
         linewidth=2, color='r')
plt.title('正态分布曲线')
plt.xlabel('x轴')
plt.ylabel('y轴')
plt.show()
