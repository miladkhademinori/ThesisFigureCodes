import numpy as np
import matplotlib.pyplot as plt

# Create data

g1 = (200*np.random.rand(1000), 200*np.random.rand(1000))
g2 = (0, 0)

data = (g1, g2)
colors = ("red", "black")
groups = ("Nodes", "Base Station")

# Create plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, facecolor="1.0")

for data, color, group in zip(data, colors, groups):
    x, y = data
    ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=20, label=group)

ax.scatter(0, 0, alpha=0.8, c="black", edgecolors='none', s=160)


#plt.title('Matplot scatter plot')
plt.legend(loc=2)
plt.savefig('/home/milad/Desktop/AUT-THESIS/figures/UniformDistribution.png')
plt.show()