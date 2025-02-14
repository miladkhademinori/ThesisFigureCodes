import numpy as np
import matplotlib.pyplot as plt

# Create data
N = 500
x = 200*np.random.rand(N)
y = 200*np.random.rand(N)
colors = (0, 0, 0)
area = np.pi * 3

# Plot
plt.scatter(x, y, s=area, c=colors, alpha=0.5)

plt.xlim(0, 250)
plt.ylim(0, 250)

#plt.title('Scatter plot pythonspot.com')
#plt.xlabel('x')
#plt.ylabel('y')
plt.show()