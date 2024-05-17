import matplotlib.pyplot as plt
import numpy as np

a_values = [3, 3, 5, 5]
b_values = [2, 4, 4, 6]

t = np.linspace(0, 2 * np.pi, 1000)
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

for ax, a, b in zip(axs.flat, a_values, b_values):
    x = np.sin(a * t)
    y = np.sin(b * t)
    ax.plot(x, y)
    ax.set_title(f'Lissajous Figure (a={a}, b={b})')
    ax.grid(True)

plt.tight_layout()
plt.show()