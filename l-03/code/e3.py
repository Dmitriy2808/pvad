import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

xs = np.array([0, 0.5, 1, 2, 3, 3.5, 4,   5, 6,   6.5, 7, 8, 9, 9.5, 10])
ys = np.array([0, 0.3, 1, 3, 1, 0.3, 0.1, 1, 0.1, 0.3, 1, 3, 1, 0.3, 0])

f = interp1d(xs, ys, kind="cubic")
xis = np.linspace(0, xs[-1], 1000)
yis = f(xis)

yis = yis / (sum(yis) * 10/1000)

F = []
prev = 0
for y in yis:
    s = y * 0.01
    F.append(prev + s)
    prev += s

plt.plot(xis, F, "b")
plt.grid(True)
plt.savefig("e3.png")
