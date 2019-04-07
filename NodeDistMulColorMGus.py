import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


# Create data

g1 = ([stats.truncnorm.rvs((-50 - 0) / 20, (50 - 0) / 20, loc=50, scale=20, size=200),
       stats.truncnorm.rvs((-50 - 0) / 20, (50 - 0) / 20, loc=50, scale=20, size=200),
       stats.truncnorm.rvs((-50 - 0) / 20, (50 - 0) / 20, loc=100, scale=20, size=200),
       stats.truncnorm.rvs((-50 - 0) / 20, (50 - 0) / 20, loc=150, scale=20, size=200),
       stats.truncnorm.rvs((-50 - 0) / 20, (50 - 0) / 20, loc=150, scale=20, size=200)],

      [stats.truncnorm.rvs((-50 - 0) / 20, (50 - 0) / 20, loc=50, scale=20, size=200),
       stats.truncnorm.rvs((-50 - 0) / 20, (50 - 0) / 20, loc=150, scale=20, size=200),
       stats.truncnorm.rvs((-50 - 0) / 20, (50 - 0) / 20, loc=100, scale=20, size=200),
       stats.truncnorm.rvs((-50 - 0) / 20, (50 - 0) / 20, loc=50, scale=20, size=200),
       stats.truncnorm.rvs((-50 - 0) / 20, (50 - 0) / 20, loc=150, scale=20, size=200)])


g = (0, 0)


data = (g1, g)
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
plt.savefig('/home/milad/Desktop/AUT-THESIS/figures/MulGassDistribution.png')
plt.show()