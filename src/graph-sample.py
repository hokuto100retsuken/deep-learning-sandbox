import numpy as np
import matplotlib.pyplot as plt

# データ作成
x = np.arange(0, 6, 0.1)
y = np.sin(x)

plt.plot(x, y)
plt.show()
