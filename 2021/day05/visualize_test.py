import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randint(10, size=(10,8))

print(data)

ax = sns.heatmap(data, annot=True, fmt="d", cbar=None)

plt.title("How to visualize (plot) \n a numpy array in python using seaborn ?",fontsize=12)

plt.savefig("visualize_numpy_array_02.png", bbox_inches='tight', dpi=100, )

plt.show()