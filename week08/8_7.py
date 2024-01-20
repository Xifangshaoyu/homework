import matplotlib.pyplot as plt
import numpy as np

# 生成示例数据集
x = np.arange(1, 11)
y = np.array([20, 44, 13, 74, 52, 23, 82, 31, 62, 92])

# 绘制折线图
plt.figure(figsize=(20, 12))
plt.subplot(1, 3, 1)
plt.plot(x, y, marker='o')
plt.title('折线图')

# 绘制散点图
plt.subplot(1, 3, 2)
plt.scatter(x, y, color='red')
plt.title('散点图')

# 绘制柱状图
plt.subplot(1, 3, 3)
plt.bar(x, y, color='green')
plt.title('柱状图')

plt.tight_layout()
plt.show()