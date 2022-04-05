import numpy as np
import matplotlib.pyplot as plt

v = np.array([2, -1])
plt.plot([0,v[0]], [0,v[1]])
plt.axis([-3,3,-3,3])

print(v)
print(plt.plot)
print(plt.axis)
