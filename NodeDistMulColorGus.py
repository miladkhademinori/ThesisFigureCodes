import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


# Create data

g1 = (stats.truncnorm.rvs((0 - 0) / 100, (200 - 0) / 100, loc=0, scale=100, size=1000),
      stats.truncnorm.rvs((0 - 0) / 100, (200 - 0) /100, loc=0, scale=100, size=1000))
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
plt.savefig('/home/milad/Desktop/AUT-THESIS/figures/GassDistribution.png')
plt.show()