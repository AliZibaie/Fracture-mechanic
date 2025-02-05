import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

theta = np.linspace(0, 2 * np.pi, 100)
d = 0.005
KI = 28
ay = 300
v = 0.34

r1 = (0.5 + 0.5 * np.cos(theta) + 1.5 * (np.sin(theta) ** 2)) * (1 / (2 * np.pi) * (KI / ay) ** 2)
r2 = (((1 - v ** 2) / 2) * (1 + np.cos(theta)) + (3 / 4) * (np.sin(theta) ** 2)) * (1 / (2 * np.pi) * (KI / ay) ** 2)

x1 = r1 * np.cos(theta)
y1 = np.zeros_like(theta)
z1 = r1 * np.sin(theta)

x2 = r2 * np.cos(theta)
y2 = d * np.ones_like(theta)
z2 = r2 * np.sin(theta)

x3 = r2 * np.cos(theta)
y3 = 4 * d * np.ones_like(theta)
z3 = r2 * np.sin(theta)

x4 = r1 * np.cos(theta)
y4 = 5 * d * np.ones_like(theta)
z4 = r1 * np.sin(theta)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x1, y1, z1, 'b', linewidth=2)
ax.plot(x2, y2, z2, 'r', linewidth=2)
ax.plot(x3, y3, z3, 'r', linewidth=2)
ax.plot(x4, y4, z4, 'b', linewidth=2)

for i in range(len(theta)):
    for j in range(3):
        ax.plot([x1[i], x2[i]], [y1[i], y2[i]], [z1[i], z2[i]], 'k')
        ax.plot([x2[i], x3[i]], [y2[i], y3[i]], [z2[i], z3[i]], 'k')
        ax.plot([x3[i], x4[i]], [y3[i], y4[i]], [z3[i], z4[i]], 'k')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.grid(True)
ax.set_title('')

plt.show()
